import os
import sys
import unittest
import grpc
from google.protobuf.descriptor import FieldDescriptor

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GENERATED_DIR = os.path.join(ROOT_DIR, "src", "generated")
if GENERATED_DIR not in sys.path:
    sys.path.insert(0, GENERATED_DIR)

import bolsa_uteq_pb2
import bolsa_uteq_pb2_grpc


class TestContratosGrpc(unittest.TestCase):
    """Validación de contratos Protobuf y stubs gRPC generados desde proto/bolsa_uteq.proto."""

    def test_descriptor_paquete_y_servicio_perfil(self):
        file_descriptor = bolsa_uteq_pb2.DESCRIPTOR
        self.assertEqual(file_descriptor.package, "bolsa_uteq")
        self.assertIn("PerfilService", file_descriptor.services_by_name)

        servicio = file_descriptor.services_by_name["PerfilService"]
        self.assertIn("VerificarElegibilidad", servicio.methods_by_name)

        metodo = servicio.methods_by_name["VerificarElegibilidad"]
        self.assertEqual(metodo.input_type.name, "ConsultaGraduadoRequest")
        self.assertEqual(metodo.output_type.name, "ElegibilidadResponse")

    def test_descriptor_consulta_graduado_request(self):
        descriptor = bolsa_uteq_pb2.ConsultaGraduadoRequest.DESCRIPTOR
        self.assertEqual(descriptor.full_name, "bolsa_uteq.ConsultaGraduadoRequest")

        campos_esperados = {
            "cedula_o_id": (1, FieldDescriptor.TYPE_STRING),
            "codigo_oferta": (2, FieldDescriptor.TYPE_STRING),
        }
        campos_actuales = {
            campo.name: (campo.number, campo.type) for campo in descriptor.fields
        }
        self.assertEqual(campos_actuales, campos_esperados)

    def test_descriptor_elegibilidad_response(self):
        descriptor = bolsa_uteq_pb2.ElegibilidadResponse.DESCRIPTOR
        self.assertEqual(descriptor.full_name, "bolsa_uteq.ElegibilidadResponse")

        campos_esperados = {
            "elegible": (1, FieldDescriptor.TYPE_BOOL),
            "nombre_completo": (2, FieldDescriptor.TYPE_STRING),
            "carrera": (3, FieldDescriptor.TYPE_STRING),
            "motivo": (4, FieldDescriptor.TYPE_STRING),
        }
        campos_actuales = {
            campo.name: (campo.number, campo.type) for campo in descriptor.fields
        }
        self.assertEqual(campos_actuales, campos_esperados)

    def test_stub_expone_rpc_verificar_elegibilidad(self):
        with grpc.insecure_channel("127.0.0.1:50055") as canal:
            stub = bolsa_uteq_pb2_grpc.PerfilServiceStub(canal)
            self.assertTrue(hasattr(stub, "VerificarElegibilidad"))
            self.assertTrue(callable(stub.VerificarElegibilidad))

    def test_serializacion_deserializacion_consulta_graduado_request(self):
        original = bolsa_uteq_pb2.ConsultaGraduadoRequest(
            cedula_o_id="GRAD-TEST-001",
            codigo_oferta="OF-2026-001",
        )
        payload = original.SerializeToString()
        self.assertIsInstance(payload, bytes)
        self.assertGreater(len(payload), 0)

        reconstruido = bolsa_uteq_pb2.ConsultaGraduadoRequest()
        reconstruido.ParseFromString(payload)

        self.assertEqual(reconstruido.cedula_o_id, original.cedula_o_id)
        self.assertEqual(reconstruido.codigo_oferta, original.codigo_oferta)
        self.assertEqual(reconstruido, original)

    def test_serializacion_deserializacion_elegibilidad_response(self):
        casos = [
            bolsa_uteq_pb2.ElegibilidadResponse(
                elegible=True,
                nombre_completo="Kenny Isaías España Vera",
                carrera="Ingeniería en Software",
                motivo="Graduado verificado y habilitado para postular.",
            ),
            bolsa_uteq_pb2.ElegibilidadResponse(
                elegible=False,
                nombre_completo="No registrado",
                carrera="N/A",
                motivo="Graduado no encontrado en el padrón de la UTEQ.",
            ),
        ]

        for original in casos:
            with self.subTest(elegible=original.elegible):
                payload = original.SerializeToString()
                self.assertIsInstance(payload, bytes)
                self.assertGreater(len(payload), 0)

                reconstruido = bolsa_uteq_pb2.ElegibilidadResponse()
                reconstruido.ParseFromString(payload)

                self.assertEqual(reconstruido.elegible, original.elegible)
                self.assertEqual(reconstruido.nombre_completo, original.nombre_completo)
                self.assertEqual(reconstruido.carrera, original.carrera)
                self.assertEqual(reconstruido.motivo, original.motivo)
                self.assertEqual(reconstruido, original)


if __name__ == "__main__":
    unittest.main()
