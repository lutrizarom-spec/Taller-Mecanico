import unittest
from src.usuario import Usuario
from src.auto import Auto
from src.excepciones import DeudaPendienteError


class TestUsuario(unittest.TestCase):
    """Casos de prueba para el comportamiento comercial y restricciones de Usuario."""

    def setUp(self) -> None:
        self.usuario = Usuario(rut="12345678-9", nombre="Carlos Pérez", deuda=0)
        self.auto = Auto(patente="AUTO12", anio=2021)
        self.auto.ingresar()  # El vehículo inicia dentro del taller

    def test_creacion_valida(self) -> None:
        self.assertEqual(self.usuario.rut, "12345678-9")
        self.assertEqual(self.usuario.nombre, "Carlos Pérez")
        self.assertEqual(self.usuario.deuda, 0)

    def test_registrar_y_pagar_deuda(self) -> None:
        self.usuario.registrar_deuda(15000)
        self.assertEqual(self.usuario.deuda, 15000)

        vuelto = self.usuario.pagar_deuda(5000)
        self.assertEqual(self.usuario.deuda, 10000)
        self.assertEqual(vuelto, 0)

        vuelto = self.usuario.pagar_deuda(12000)
        self.assertEqual(self.usuario.deuda, 0)
        self.assertEqual(vuelto, 2000)

    def test_retirar_vehiculo_sin_deuda_exitoso(self) -> None:
        mensaje = self.usuario.retirar_vehiculo(self.auto)
        self.assertEqual(mensaje, "El vehículo ha sido entregado.")
        self.assertFalse(self.auto.en_taller)

    def test_retirar_vehiculo_con_deuda_lanza_excepcion(self) -> None:
        self.usuario.registrar_deuda(45000)

        with self.assertRaises(DeudaPendienteError) as ctx:
            self.usuario.retirar_vehiculo(self.auto)

        self.assertEqual(ctx.exception.deuda, 45000)
        self.assertIn("presenta una deuda", str(ctx.exception))
        # El vehículo debe continuar en taller
        self.assertTrue(self.auto.en_taller)

    def test_retirar_tras_saldar_deuda(self) -> None:
        self.usuario.registrar_deuda(20000)

        # Intento bloqueado
        with self.assertRaises(DeudaPendienteError):
            self.usuario.retirar_vehiculo(self.auto)
        self.assertTrue(self.auto.en_taller)

        # Paga deuda y ahora sí retira
        self.usuario.pagar_deuda(20000)
        mensaje = self.usuario.retirar_vehiculo(self.auto)
        self.assertEqual(mensaje, "El vehículo ha sido entregado.")
        self.assertFalse(self.auto.en_taller)

    def test_validaciones_invalido(self) -> None:
        with self.assertRaises(ValueError):
            Usuario(rut="", nombre="Ana", deuda=0)

        with self.assertRaises(ValueError):
            Usuario(rut="98765432-1", nombre="   ", deuda=0)

        with self.assertRaises(ValueError):
            Usuario(rut="98765432-1", nombre="Ana", deuda=-500)

        with self.assertRaises(TypeError):
            self.usuario.retirar_vehiculo("no_es_vehiculo")  # type: ignore


if __name__ == "__main__":
    unittest.main()
