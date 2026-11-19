from concurrent import futures
import math
import os
import sys
import time
import unittest
import grpc

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GENERATED_DIR = os.path.join(ROOT_DIR, "src", "generated")
SERVICIO_PERFILES_DIR = os.path.join(ROOT_DIR, "src", "servicio_perfiles")

for ruta in (GENERATED_DIR, SERVICIO_PERFILES_DIR):
    if ruta not in sys.path:
        sys.path.insert(0, ruta)

import bolsa_uteq_pb2
import bolsa_uteq_pb2_grpc
from servidor_perfiles import GRADUADOS_UTEQ, PerfilServicer


class TestIntegracionPerfilesGrpc(unittest.TestCase):
    """Pruebas de integración, latencia p95 y disponibilidad concurrente sobre PerfilService."""

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
            cls._server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
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

    @classmethod
    def tearDownClass(cls):
        if cls._channel is not None:
            cls._channel.close()
        if cls._server is not None:
            cls._server.stop(grace=1).wait()

    def test_consulta_graduado_habilitado(self):
        cedula_real = "0000000001"
        esperado = GRADUADOS_UTEQ[cedula_real]

        solicitud = bolsa_uteq_pb2.ConsultaGraduadoRequest(
            cedula_o_id=cedula_real,
            codigo_oferta="OF-2026-001",
        )
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
            cedula_o_id="9999999999",
            codigo_oferta="OF-2026-001",
        )
        respuesta = self._stub.VerificarElegibilidad(solicitud, timeout=5)

        self.assertFalse(respuesta.elegible)
        self.assertEqual(respuesta.nombre_completo, "No registrado")
        self.assertEqual(respuesta.carrera, "N/A")
        self.assertEqual(
            respuesta.motivo,
            "Graduado no encontrado en el padrón de la UTEQ.",
        )

    def test_latencia_p95_bajo_umbral(self):
        total_llamadas = 30
        solicitud = bolsa_uteq_pb2.ConsultaGraduadoRequest(
            cedula_o_id="0000000002",
            codigo_oferta="OF-2026-001",
        )
        latencias_ms = []

        for _ in range(total_llamadas):
            inicio = time.perf_counter()
            respuesta = self._stub.VerificarElegibilidad(solicitud, timeout=5)
            fin = time.perf_counter()
            self.assertTrue(respuesta.elegible)
            latencias_ms.append((fin - inicio) * 1000.0)

        latencias_ordenadas = sorted(latencias_ms)
        promedio_ms = sum(latencias_ms) / len(latencias_ms)
        indice_p95 = math.ceil(0.95 * len(latencias_ordenadas)) - 1
        p95_ms = latencias_ordenadas[indice_p95]

        print(
            f"\n[Métrica Latencia] Target={self._target} | Llamadas={total_llamadas} | "
            f"Promedio={promedio_ms:.3f} ms | p95={p95_ms:.3f} ms (umbral < 300.0 ms)",
            flush=True,
        )
        self.assertLess(p95_ms, 300.0)

    def test_disponibilidad_concurrencia(self):
        total_solicitudes = 20
        cedulas_reales = list(GRADUADOS_UTEQ.keys())

        def invocar(indice: int):
            cedula = cedulas_reales[indice % len(cedulas_reales)]
            solicitud = bolsa_uteq_pb2.ConsultaGraduadoRequest(
                cedula_o_id=cedula,
                codigo_oferta=f"OF-2026-{indice + 1:03d}",
            )
            respuesta = self._stub.VerificarElegibilidad(solicitud, timeout=5)
            return respuesta.elegible

        exitosas = 0
        errores = []

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


if __name__ == "__main__":
    unittest.main()
