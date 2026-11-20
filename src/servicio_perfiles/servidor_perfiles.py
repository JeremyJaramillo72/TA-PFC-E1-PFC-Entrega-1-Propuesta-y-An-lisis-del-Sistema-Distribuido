from concurrent import futures
from datetime import datetime
import os
import re
import socket
import sys
import grpc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "generated")))
import bolsa_uteq_pb2
import bolsa_uteq_pb2_grpc

# Padrón inicial en memoria para validar la comunicación gRPC del esqueleto (E1).
# Solo se usan identificadores ficticios con formato GRAD-TEST-NNN; nunca cédulas reales.
GRADUADOS_UTEQ = {
    "GRAD-TEST-001": {
        "nombre": "Luis Jeremy Jaramillo Acosta",
        "carrera": "Ingeniería en Software",
        "habilitado": True,
    },
    "GRAD-TEST-002": {
        "nombre": "Kenny Isaías España Vera",
        "carrera": "Ingeniería en Software",
        "habilitado": True,
    },
    "GRAD-TEST-003": {
        "nombre": "Luis Paca",
        "carrera": "Ingeniería en Software",
        "habilitado": True,
    },
}

# Formato aceptado del identificador: prefijo GRAD- seguido de bloques alfanuméricos
# en mayúsculas separados por guiones (p. ej. GRAD-TEST-001), máximo 32 caracteres.
PATRON_ID_GRADUADO = re.compile(r"GRAD(?:-[A-Z0-9]+)+")
LONGITUD_MAXIMA_ID = 32


def validar_id_graduado(cedula_o_id: str):
    """Devuelve un mensaje de error si el identificador es inválido, o None si es correcto."""
    if not cedula_o_id or not cedula_o_id.strip():
        return "El identificador del graduado es obligatorio y no puede estar vacío."
    if len(cedula_o_id) > LONGITUD_MAXIMA_ID or not PATRON_ID_GRADUADO.fullmatch(cedula_o_id):
        return (
            f"Identificador mal formado: '{cedula_o_id}'. "
            "Se espera el formato GRAD-XXXX-NNN (ej. GRAD-TEST-001)."
        )
    return None


class PerfilServicer(bolsa_uteq_pb2_grpc.PerfilServiceServicer):
    def VerificarElegibilidad(self, request, context):
        hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(
            f"[{hora}] [servicio-perfiles] Solicitud recibida | "
            f"ID={request.cedula_o_id!r} | Oferta={request.codigo_oferta!r}"
        )

        error_validacion = validar_id_graduado(request.cedula_o_id)
        if error_validacion:
            print(f"[{hora}] [servicio-perfiles] INVALID_ARGUMENT | {error_validacion}")
            # abort() lanza una excepción y termina la llamada con el código indicado
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, error_validacion)

        graduado = GRADUADOS_UTEQ.get(request.cedula_o_id)

        if not graduado:
            return bolsa_uteq_pb2.ElegibilidadResponse(
                elegible=False,
                nombre_completo="No registrado",
                carrera="N/A",
                motivo="Graduado no encontrado en el padrón de la UTEQ.",
            )

        return bolsa_uteq_pb2.ElegibilidadResponse(
            elegible=graduado["habilitado"],
            nombre_completo=graduado["nombre"],
            carrera=graduado["carrera"],
            motivo="Graduado verificado y habilitado para postular.",
        )


def iniciar_servidor(puerto: int = 50051) -> None:
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    bolsa_uteq_pb2_grpc.add_PerfilServiceServicer_to_server(PerfilServicer(), servidor)
    servidor.add_insecure_port(f"[::]:{puerto}")
    servidor.start()
    print(
        f"[servicio-perfiles] Escuchando gRPC en puerto {puerto} | "
        f"Equipo={socket.gethostname()} | PID={os.getpid()}"
    )
    servidor.wait_for_termination()


if __name__ == "__main__":
    iniciar_servidor()
