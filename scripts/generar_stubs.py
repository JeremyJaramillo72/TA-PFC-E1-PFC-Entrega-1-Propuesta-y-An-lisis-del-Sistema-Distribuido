"""Regenera los stubs gRPC de Python a partir de proto/bolsa_uteq.proto.

Uso (desde la raíz del repositorio):
    python scripts/generar_stubs.py
    python scripts/generar_stubs.py --salida <carpeta>   # p. ej. para comparar sin sobrescribir
"""
import argparse
import os
import sys

from grpc_tools import protoc
import grpc_tools

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DIR_PROTO = os.path.join(RAIZ, "proto")
ARCHIVO_PROTO = os.path.join(DIR_PROTO, "bolsa_uteq.proto")
DIR_SALIDA_DEFECTO = os.path.join(RAIZ, "src", "generated")
# Incluye los .proto estándar de Google (timestamp, empty, etc.) por si el contrato los importa
DIR_PROTO_ESTANDAR = os.path.join(os.path.dirname(grpc_tools.__file__), "_proto")


def generar_stubs(dir_salida: str) -> int:
    if not os.path.isfile(ARCHIVO_PROTO):
        print(f"[generar-stubs] No se encontró el contrato: {ARCHIVO_PROTO}")
        return 1

    os.makedirs(dir_salida, exist_ok=True)
    argumentos = [
        "grpc_tools.protoc",
        f"-I{DIR_PROTO}",
        f"-I{DIR_PROTO_ESTANDAR}",
        f"--python_out={dir_salida}",
        f"--grpc_python_out={dir_salida}",
        ARCHIVO_PROTO,
    ]
    codigo = protoc.main(argumentos)
    if codigo != 0:
        print(f"[generar-stubs] protoc terminó con código {codigo}")
        return codigo

    init = os.path.join(dir_salida, "__init__.py")
    if not os.path.exists(init):
        open(init, "w", encoding="utf-8").close()

    print(f"[generar-stubs] Stubs generados en {dir_salida}:")
    for nombre in ("bolsa_uteq_pb2.py", "bolsa_uteq_pb2_grpc.py"):
        ruta = os.path.join(dir_salida, nombre)
        estado = "OK" if os.path.isfile(ruta) else "FALTA"
        print(f"  - {nombre}: {estado}")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compila proto/bolsa_uteq.proto a stubs gRPC de Python.")
    parser.add_argument("--salida", default=DIR_SALIDA_DEFECTO, help="Carpeta destino (por defecto src/generated)")
    sys.exit(generar_stubs(os.path.abspath(parser.parse_args().salida)))
