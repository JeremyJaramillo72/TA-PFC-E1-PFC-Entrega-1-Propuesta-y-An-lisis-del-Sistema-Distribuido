from concurrent import futures
from datetime import datetime
import os
import socket
import sys
import grpc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "generated")))
import bolsa_uteq_pb2
import bolsa_uteq_pb2_grpc

# Padrón inicial en memoria para validar la comunicación gRPC del esqueleto (E1)
GRADUADOS_UTEQ = {
    # Identificador genérico de prueba utilizado únicamente para fines demostrativos del código
    "0000000001": {
        "nombre": "Luis Jeremy Jaramillo Acosta",
        "carrera": "Ingeniería en Software",
        "habilitado": True,
    },
    # Identificador genérico de prueba utilizado únicamente para fines demostrativos del código
    "0000000002": {
        "nombre": "Kenny Isaías España Vera",
        "carrera": "Ingeniería en Software",
        "habilitado": True,
    },
    # Identificador genérico de prueba utilizado únicamente para fines demostrativos del código
    "0000000003": {
        "nombre": "Luis Paca",
        "carrera": "Ingeniería en Software",
        "habilitado": True,
    },
}


class PerfilServicer(bolsa_uteq_pb2_grpc.PerfilServiceServicer):
    def VerificarElegibilidad(self, request, context):
        graduado = GRADUADOS_UTEQ.get(request.cedula_o_id)
        hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(
            f"[{hora}] [servicio-perfiles] Solicitud recibida | "
            f"ID={request.cedula_o_id} | Oferta={request.codigo_oferta}"
        )

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
