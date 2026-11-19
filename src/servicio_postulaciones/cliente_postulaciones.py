from datetime import datetime
import os
import socket
import sys
import grpc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "generated")))
import bolsa_uteq_pb2
import bolsa_uteq_pb2_grpc

DIRECCION_PERFILES = os.getenv("PERFILES_ADDR", "localhost:50051")
TIEMPO_ESPERA_SEG = 5

# Casos de prueba del esqueleto (E1): un graduado habilitado y una cédula no registrada
CASOS_PRUEBA = [
    # Cédula de prueba utilizada únicamente para fines demostrativos del código
    {"cedula_o_id": "1206983421", "codigo_oferta": "OF-2026-001"},
    # Cédula ficticia que no existe en el padrón, para validar el caso negativo
    {"cedula_o_id": "0999999999", "codigo_oferta": "OF-2026-001"},
]


def verificar_elegibilidad(stub, cedula_o_id: str, codigo_oferta: str) -> None:
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(
        f"[{hora}] [servicio-postulaciones] Enviando consulta | "
        f"ID={cedula_o_id} | Oferta={codigo_oferta}"
    )
    solicitud = bolsa_uteq_pb2.ConsultaGraduadoRequest(
        cedula_o_id=cedula_o_id,
        codigo_oferta=codigo_oferta,
    )
    try:
        respuesta = stub.VerificarElegibilidad(solicitud, timeout=TIEMPO_ESPERA_SEG)
    except grpc.RpcError as error:
        print(
            f"[servicio-postulaciones] Error gRPC: {error.code().name} | {error.details()}"
        )
        return

    estado = "ELEGIBLE" if respuesta.elegible else "NO ELEGIBLE"
    print(
        f"[servicio-postulaciones] Respuesta: {estado} | "
        f"Nombre={respuesta.nombre_completo} | Carrera={respuesta.carrera} | "
        f"Motivo={respuesta.motivo}"
    )


def ejecutar_cliente() -> None:
    print(
        f"[servicio-postulaciones] Conectando a servicio-perfiles en {DIRECCION_PERFILES} | "
        f"Equipo={socket.gethostname()} | PID={os.getpid()}"
    )
    with grpc.insecure_channel(DIRECCION_PERFILES) as canal:
        stub = bolsa_uteq_pb2_grpc.PerfilServiceStub(canal)
        for caso in CASOS_PRUEBA:
            verificar_elegibilidad(stub, caso["cedula_o_id"], caso["codigo_oferta"])


if __name__ == "__main__":
    ejecutar_cliente()
