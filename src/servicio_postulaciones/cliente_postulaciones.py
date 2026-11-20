from datetime import datetime
import os
import socket
import sys
import threading
import grpc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "generated")))
import bolsa_uteq_pb2
import bolsa_uteq_pb2_grpc

DIRECCION_PERFILES = os.getenv("PERFILES_ADDR", "localhost:50051")
# Deadline explícito por llamada RPC: si servicio-perfiles no responde a tiempo,
# gRPC cancela la llamada con DEADLINE_EXCEEDED en lugar de bloquear la postulación.
TIEMPO_ESPERA_SEG = 2.0

# Mensajes de usuario para los códigos gRPC que el esqueleto maneja de forma explícita
MENSAJES_ERROR_GRPC = {
    grpc.StatusCode.UNAVAILABLE: "servicio-perfiles no disponible (¿está iniciado el servidor?).",
    grpc.StatusCode.DEADLINE_EXCEEDED: f"servicio-perfiles no respondió en {TIEMPO_ESPERA_SEG} s.",
    grpc.StatusCode.INVALID_ARGUMENT: "la solicitud fue rechazada por datos inválidos.",
}

# Casos de prueba del esqueleto (E1). Solo se usan identificadores ficticios GRAD-TEST-NNN.
CASOS_PRUEBA = [
    ("(a) Postulación exitosa con ID ficticio válido", "GRAD-TEST-002", "OF-2026-001"),
    ("(b) Reintento duplicado del mismo graduado a la misma oferta (RNF-05)", "GRAD-TEST-002", "OF-2026-001"),
    ("(c) Identificador mal formado (INVALID_ARGUMENT)", "ID-INVALIDO", "OF-2026-001"),
    ("(c) Identificador vacío (INVALID_ARGUMENT)", "", "OF-2026-001"),
    ("(d) Graduado con formato válido pero no registrado", "GRAD-TEST-999", "OF-2026-001"),
]


def _hora() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class RegistroPostulaciones:
    """Registro en memoria de postulaciones aceptadas, indexado por (id_graduado, codigo_oferta).

    Garantiza RNF-05: un reintento del mismo graduado a la misma oferta no genera
    una segunda postulación (operación idempotente).
    """

    def __init__(self):
        self._aceptadas = set()
        self._candado = threading.Lock()

    def existe(self, id_graduado: str, codigo_oferta: str) -> bool:
        with self._candado:
            return (id_graduado, codigo_oferta) in self._aceptadas

    def registrar(self, id_graduado: str, codigo_oferta: str) -> bool:
        """Registra la postulación; devuelve False si ya existía."""
        clave = (id_graduado, codigo_oferta)
        with self._candado:
            if clave in self._aceptadas:
                return False
            self._aceptadas.add(clave)
            return True

    def listar(self):
        with self._candado:
            return sorted(self._aceptadas)


def verificar_elegibilidad(stub, cedula_o_id: str, codigo_oferta: str):
    """Invoca VerificarElegibilidad con deadline explícito.

    Devuelve la ElegibilidadResponse, o None si la llamada terminó en error gRPC
    (el error se informa por consola sin propagar la excepción).
    """
    print(
        f"[{_hora()}] [servicio-postulaciones] Enviando consulta | "
        f"ID={cedula_o_id!r} | Oferta={codigo_oferta!r} | Timeout={TIEMPO_ESPERA_SEG}s"
    )
    solicitud = bolsa_uteq_pb2.ConsultaGraduadoRequest(
        cedula_o_id=cedula_o_id,
        codigo_oferta=codigo_oferta,
    )
    try:
        respuesta = stub.VerificarElegibilidad(solicitud, timeout=TIEMPO_ESPERA_SEG)
    except grpc.RpcError as error:
        codigo = error.code()
        explicacion = MENSAJES_ERROR_GRPC.get(codigo, "error gRPC no previsto.")
        print(
            f"[servicio-postulaciones] Error gRPC: {codigo.name} | {error.details()} | {explicacion}"
        )
        return None

    estado = "ELEGIBLE" if respuesta.elegible else "NO ELEGIBLE"
    print(
        f"[servicio-postulaciones] Respuesta: {estado} | "
        f"Nombre={respuesta.nombre_completo} | Carrera={respuesta.carrera} | "
        f"Motivo={respuesta.motivo}"
    )
    return respuesta


def postular(stub, registro: RegistroPostulaciones, id_graduado: str, codigo_oferta: str) -> str:
    """Intenta registrar una postulación y devuelve el resultado: ACEPTADA, DUPLICADA o RECHAZADA."""
    if registro.existe(id_graduado, codigo_oferta):
        print(
            f"[servicio-postulaciones] Postulación DUPLICADA (RNF-05) | "
            f"{id_graduado} ya postuló a {codigo_oferta}; no se registra de nuevo."
        )
        return "DUPLICADA"

    respuesta = verificar_elegibilidad(stub, id_graduado, codigo_oferta)
    if respuesta is None or not respuesta.elegible:
        print("[servicio-postulaciones] Postulación RECHAZADA.")
        return "RECHAZADA"

    if not registro.registrar(id_graduado, codigo_oferta):
        # Otro hilo registró la misma postulación mientras se verificaba la elegibilidad
        print(f"[servicio-postulaciones] Postulación DUPLICADA (RNF-05) | {id_graduado} -> {codigo_oferta}")
        return "DUPLICADA"

    print(f"[servicio-postulaciones] Postulación ACEPTADA | {id_graduado} -> {codigo_oferta}")
    return "ACEPTADA"


def ejecutar_cliente() -> None:
    print(
        f"[servicio-postulaciones] Conectando a servicio-perfiles en {DIRECCION_PERFILES} | "
        f"Equipo={socket.gethostname()} | PID={os.getpid()}"
    )
    registro = RegistroPostulaciones()
    resultados = []

    with grpc.insecure_channel(DIRECCION_PERFILES) as canal:
        stub = bolsa_uteq_pb2_grpc.PerfilServiceStub(canal)
        for descripcion, id_graduado, codigo_oferta in CASOS_PRUEBA:
            print(f"\n--- {descripcion} ---")
            resultados.append((descripcion, postular(stub, registro, id_graduado, codigo_oferta)))

    print("\n=== Resumen de casos ===")
    for descripcion, resultado in resultados:
        print(f"  {resultado:<10} {descripcion}")
    print(f"Postulaciones registradas en memoria: {registro.listar()}")


if __name__ == "__main__":
    ejecutar_cliente()
