from concurrent import futures
import contextlib
import io
import math
import os
import socket
import sys
import threading
import time
import unittest
import grpc

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GENERATED_DIR = os.path.join(ROOT_DIR, "src", "generated")
SERVICIO_PERFILES_DIR = os.path.join(ROOT_DIR, "src", "servicio_perfiles")
SERVICIO_POSTULACIONES_DIR = os.path.join(ROOT_DIR, "src", "servicio_postulaciones")

for ruta in (GENERATED_DIR, SERVICIO_PERFILES_DIR, SERVICIO_POSTULACIONES_DIR):
    if ruta not in sys.path:
        sys.path.insert(0, ruta)

import bolsa_uteq_pb2
import bolsa_uteq_pb2_grpc
from cliente_postulaciones import verificar_elegibilidad
from servidor_perfiles import GRADUADOS_UTEQ, PerfilServicer


def _percentil(valores_ordenados, p: float) -> float:
    indice = max(0, math.ceil((p / 100.0) * len(valores_ordenados)) - 1)
    return valores_ordenados[indice]


class _ServicerConRetardo(bolsa_uteq_pb2_grpc.PerfilServiceServicer):
    """Servicer auxiliar para validar vencimiento controlado de deadline gRPC."""

    def __init__(self, retardo_seg: float = 0.6):
        self._retardo_seg = retardo_seg

    def VerificarElegibilidad(self, request, context):
        time.sleep(self._retardo_seg)
        return bolsa_uteq_pb2.ElegibilidadResponse(
            elegible=False,
            nombre_completo="Timeout simulado",
            carrera="N/A",
            motivo="Respuesta tardía para prueba de deadline.",
        )


class TestIntegracionPerfilesGrpc(unittest.TestCase):
    """Pruebas de integración, carga (RNF-01), disponibilidad y resiliencia sobre PerfilService."""

    _server = None
    _channel = None
    _stub = None
    _target = None

    @classmethod
    def setUpClass(cls):
        env_target = os.getenv("GRPC_TARGET", "").strip()
        if env_target:
            cls._target = env_target
        else:
            cls._server = grpc.server(futures.ThreadPoolExecutor(max_workers=50))
            bolsa_uteq_pb2_grpc.add_PerfilServiceServicer_to_server(
                PerfilServicer(), cls._server
            )
            puerto = cls._server.add_insecure_port("127.0.0.1:50055")
            if puerto == 0:
                puerto = cls._server.add_insecure_port("127.0.0.1:0")
            cls._server.start()
            cls._target = f"127.0.0.1:{puerto}"

        cls._channel = grpc.insecure_channel(cls._target)
        grpc.channel_ready_future(cls._channel).result(timeout=5)
        cls._stub = bolsa_uteq_pb2_grpc.PerfilServiceStub(cls._channel)
        with contextlib.redirect_stdout(io.StringIO()):
            cls._stub.VerificarElegibilidad(
                bolsa_uteq_pb2.ConsultaGraduadoRequest(
                    cedula_o_id="GRAD-TEST-001",
                    codigo_oferta="WARMUP",
                ),
                timeout=5,
            )

    @classmethod
    def tearDownClass(cls):
        if cls._channel is not None:
            cls._channel.close()
        if cls._server is not None:
            cls._server.stop(grace=1).wait()

    def test_consulta_graduado_habilitado(self):
        id_prueba = "GRAD-TEST-001"
        esperado = GRADUADOS_UTEQ[id_prueba]

        solicitud = bolsa_uteq_pb2.ConsultaGraduadoRequest(
            cedula_o_id=id_prueba,
            codigo_oferta="OF-2026-001",
        )
        with contextlib.redirect_stdout(io.StringIO()):
            respuesta = self._stub.VerificarElegibilidad(solicitud, timeout=5)

        self.assertTrue(respuesta.elegible)
        self.assertEqual(respuesta.nombre_completo, esperado["nombre"])
        self.assertEqual(respuesta.carrera, esperado["carrera"])
        self.assertEqual(
            respuesta.motivo,
            "Graduado verificado y habilitado para postular.",
        )

    def test_consulta_graduado_inexistente(self):
        solicitud = bolsa_uteq_pb2.ConsultaGraduadoRequest(
            cedula_o_id="GRAD-TEST-999",
            codigo_oferta="OF-2026-001",
        )
        with contextlib.redirect_stdout(io.StringIO()):
            respuesta = self._stub.VerificarElegibilidad(solicitud, timeout=5)

        self.assertFalse(respuesta.elegible)
        self.assertEqual(respuesta.nombre_completo, "No registrado")
        self.assertEqual(respuesta.carrera, "N/A")
        self.assertEqual(
            respuesta.motivo,
            "Graduado no encontrado en el padrón de la UTEQ.",
        )

    def test_entrada_invalida_rechazada_con_invalid_argument(self):
        casos_borde = (
            ("", ""),
            ("   ", "OF-2026-001"),
            ("ID-INVALIDO", "OF-2026-001"),
            ("1234567890", "OF-2026-001"),
            ("grad-test-001", "OF-2026-001"),
        )
        for cedula_borde, oferta_borde in casos_borde:
            with self.subTest(cedula_o_id=cedula_borde, codigo_oferta=oferta_borde):
                solicitud = bolsa_uteq_pb2.ConsultaGraduadoRequest(
                    cedula_o_id=cedula_borde,
                    codigo_oferta=oferta_borde,
                )
                with contextlib.redirect_stdout(io.StringIO()):
                    with self.assertRaises(grpc.RpcError) as contexto:
                        self._stub.VerificarElegibilidad(solicitud, timeout=5)

                self.assertEqual(
                    contexto.exception.code(), grpc.StatusCode.INVALID_ARGUMENT
                )
                self.assertTrue(contexto.exception.details())

    def test_latencia_p95_bajo_umbral(self):
        total_llamadas = 30
        solicitud = bolsa_uteq_pb2.ConsultaGraduadoRequest(
            cedula_o_id="GRAD-TEST-002",
            codigo_oferta="OF-2026-001",
        )
        latencias_ms = []

        with contextlib.redirect_stdout(io.StringIO()):
            for _ in range(total_llamadas):
                inicio = time.perf_counter()
                respuesta = self._stub.VerificarElegibilidad(solicitud, timeout=5)
                fin = time.perf_counter()
                self.assertTrue(respuesta.elegible)
                latencias_ms.append((fin - inicio) * 1000.0)

        latencias_ordenadas = sorted(latencias_ms)
        promedio_ms = sum(latencias_ms) / len(latencias_ms)
        p95_ms = _percentil(latencias_ordenadas, 95)

        print(
            f"\n[Métrica Latencia Secuencial] Target={self._target} | Llamadas={total_llamadas} | "
            f"Promedio={promedio_ms:.3f} ms | p95={p95_ms:.3f} ms (umbral <= 300.0 ms)",
            flush=True,
        )
        self.assertLessEqual(p95_ms, 300.0)

    def test_disponibilidad_concurrencia(self):
        total_solicitudes = 20
        ids_prueba = list(GRADUADOS_UTEQ.keys())

        def invocar(indice: int):
            id_prueba = ids_prueba[indice % len(ids_prueba)]
            solicitud = bolsa_uteq_pb2.ConsultaGraduadoRequest(
                cedula_o_id=id_prueba,
                codigo_oferta=f"OF-2026-{indice + 1:03d}",
            )
            respuesta = self._stub.VerificarElegibilidad(solicitud, timeout=5)
            return respuesta.elegible

        exitosas = 0
        errores = []

        with contextlib.redirect_stdout(io.StringIO()):
            with futures.ThreadPoolExecutor(max_workers=total_solicitudes) as executor:
                tareas = [executor.submit(invocar, i) for i in range(total_solicitudes)]
                for tarea in futures.as_completed(tareas):
                    try:
                        if tarea.result():
                            exitosas += 1
                    except grpc.RpcError as exc:
                        errores.append(f"{exc.code().name}: {exc.details()}")

        disponibilidad_pct = (exitosas / total_solicitudes) * 100.0
        print(
            f"\n[Métrica Disponibilidad] Target={self._target} | "
            f"Exitosas={exitosas}/{total_solicitudes} | "
            f"Disponibilidad={disponibilidad_pct:.2f}% | Errores RPC={len(errores)}",
            flush=True,
        )
        self.assertEqual(len(errores), 0, f"Se produjeron errores RPC: {errores}")
        self.assertEqual(disponibilidad_pct, 100.0)

    def test_carga_50_clientes_concurrentes_rnf01(self):
        total_clientes = 50
        ids_prueba = list(GRADUADOS_UTEQ.keys())
        barrera = threading.Barrier(total_clientes)

        def invocar_concurrente(indice: int):
            id_prueba = ids_prueba[indice % len(ids_prueba)]
            solicitud = bolsa_uteq_pb2.ConsultaGraduadoRequest(
                cedula_o_id=id_prueba,
                codigo_oferta=f"OF-RNF01-{indice + 1:03d}",
            )
            barrera.wait(timeout=5)
            inicio = time.perf_counter()
            respuesta = self._stub.VerificarElegibilidad(solicitud, timeout=5)
            fin = time.perf_counter()
            return respuesta.elegible, (fin - inicio) * 1000.0

        latencias_ms = []
        exitosas = 0
        errores = []

        with contextlib.redirect_stdout(io.StringIO()):
            with futures.ThreadPoolExecutor(max_workers=total_clientes) as executor:
                tareas = [executor.submit(invocar_concurrente, i) for i in range(total_clientes)]
                for tarea in futures.as_completed(tareas):
                    try:
                        elegible, lat_ms = tarea.result()
                        if elegible:
                            exitosas += 1
                        latencias_ms.append(lat_ms)
                    except grpc.RpcError as exc:
                        errores.append(f"{exc.code().name}: {exc.details()}")

        latencias_ordenadas = sorted(latencias_ms)
        promedio_ms = sum(latencias_ms) / len(latencias_ms)
        p50_ms = _percentil(latencias_ordenadas, 50)
        p95_ms = _percentil(latencias_ordenadas, 95)
        p99_ms = _percentil(latencias_ordenadas, 99)
        disponibilidad_pct = (exitosas / total_clientes) * 100.0

        print(
            f"\n[Métrica Carga RNF-01] Clientes concurrentes={total_clientes} | "
            f"Exitosas={exitosas}/{total_clientes} ({disponibilidad_pct:.2f}%) | "
            f"Promedio={promedio_ms:.3f} ms | p50={p50_ms:.3f} ms | "
            f"p95={p95_ms:.3f} ms | p99={p99_ms:.3f} ms (umbral <= 300.0 ms)",
            flush=True,
        )
        self.assertEqual(len(errores), 0, f"Errores bajo carga: {errores}")
        self.assertEqual(exitosas, total_clientes)
        self.assertLessEqual(p95_ms, 300.0)

    def test_tolerancia_fallo_servidor_no_disponible_y_cliente(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(("127.0.0.1", 0))
            puerto_cerrado = sock.getsockname()[1]

        solicitud = bolsa_uteq_pb2.ConsultaGraduadoRequest(
            cedula_o_id="GRAD-TEST-002",
            codigo_oferta="OF-2026-001",
        )
        with grpc.insecure_channel(f"127.0.0.1:{puerto_cerrado}") as canal_caido:
            stub_caido = bolsa_uteq_pb2_grpc.PerfilServiceStub(canal_caido)

            with self.assertRaises(grpc.RpcError) as contexto:
                stub_caido.VerificarElegibilidad(solicitud, timeout=3)
            self.assertEqual(contexto.exception.code(), grpc.StatusCode.UNAVAILABLE)

            salida_cliente = io.StringIO()
            with contextlib.redirect_stdout(salida_cliente):
                verificar_elegibilidad(stub_caido, "GRAD-TEST-002", "OF-2026-001")

            texto_cliente = salida_cliente.getvalue()
            self.assertIn("[servicio-postulaciones] Error gRPC: UNAVAILABLE", texto_cliente)

        print(
            f"\n[Resiliencia UNAVAILABLE] Puerto cerrado=127.0.0.1:{puerto_cerrado} | "
            f"Código={contexto.exception.code().name} | Cliente manejó error sin caída.",
            flush=True,
        )

    def test_control_timeout_deadline_exceeded(self):
        servidor_lento = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
        bolsa_uteq_pb2_grpc.add_PerfilServiceServicer_to_server(
            _ServicerConRetardo(retardo_seg=0.6), servidor_lento
        )
        puerto_lento = servidor_lento.add_insecure_port("127.0.0.1:0")
        servidor_lento.start()

        try:
            with grpc.insecure_channel(f"127.0.0.1:{puerto_lento}") as canal_lento:
                grpc.channel_ready_future(canal_lento).result(timeout=5)
                stub_lento = bolsa_uteq_pb2_grpc.PerfilServiceStub(canal_lento)
                solicitud = bolsa_uteq_pb2.ConsultaGraduadoRequest(
                    cedula_o_id="GRAD-TEST-001",
                    codigo_oferta="OF-2026-001",
                )
                with self.assertRaises(grpc.RpcError) as contexto:
                    stub_lento.VerificarElegibilidad(solicitud, timeout=0.1)

                self.assertEqual(
                    contexto.exception.code(), grpc.StatusCode.DEADLINE_EXCEEDED
                )
                print(
                    f"\n[Resiliencia Timeout] Target=127.0.0.1:{puerto_lento} | "
                    f"Deadline=100 ms | Código={contexto.exception.code().name}",
                    flush=True,
                )
        finally:
            servidor_lento.stop(grace=0.2).wait()


if __name__ == "__main__":
    unittest.main()
