"""
Suite de Pruebas Unitarias para la clase Vehiculo.
"""

import unittest
from src.vehiculo import Vehiculo


class TestVehiculo(unittest.TestCase):
    """Casos de prueba para el ciclo de vida y operaciones de Vehiculo."""

    def setUp(self) -> None:
        """Inicializa una instancia limpia de Vehiculo antes de cada prueba."""
        self.vehiculo = Vehiculo(patente="ABC123", anio=2020)

    def test_inicializacion(self) -> None:
        """Verifica la asignación correcta de atributos iniciales."""
        self.assertEqual(self.vehiculo.patente, "ABC123")
        self.assertEqual(self.vehiculo.anio, 2020)
        self.assertFalse(self.vehiculo.en_taller)

    def test_ingresar_exitoso(self) -> None:
        """Verifica que el ingreso cambie el estado y devuelva mensaje esperado."""
        mensaje = self.vehiculo.ingresar()
        self.assertEqual(mensaje, "El vehículo ha ingresado al taller.")
        self.assertTrue(self.vehiculo.en_taller)

    def test_ingresar_duplicado(self) -> None:
        """Verifica que no se permita ingresar un vehículo que ya está en taller."""
        self.vehiculo.ingresar()
        mensaje_reintento = self.vehiculo.ingresar()
        self.assertEqual(mensaje_reintento, "El vehículo ya se encuentra en el taller.")
        self.assertTrue(self.vehiculo.en_taller)

    def test_entregar_exitoso(self) -> None:
        """Verifica la entrega correcta tras haber ingresado."""
        self.vehiculo.ingresar()
        mensaje_entrega = self.vehiculo.entregar()
        self.assertEqual(mensaje_entrega, "El vehículo ha sido entregado.")
        self.assertFalse(self.vehiculo.en_taller)

    def test_entregar_sin_haber_ingresado(self) -> None:
        """Verifica que no se pueda entregar un vehículo fuera del taller."""
        mensaje_entrega = self.vehiculo.entregar()
        self.assertEqual(mensaje_entrega, "El vehículo no se encuentra en el taller.")
        self.assertFalse(self.vehiculo.en_taller)

    def test_tarifa_hora(self) -> None:
        """Verifica que la tarifa por hora retorne el valor monetario esperado."""
        self.assertEqual(self.vehiculo.tarifa_hora(), 5000)


if __name__ == "__main__":
    unittest.main()
