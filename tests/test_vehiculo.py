"""
Suite de Pruebas Unitarias para Vehiculo y Clases Hijas.
"""

import unittest
from src.vehiculo import Vehiculo
from src.auto import Auto
from src.moto import Moto
from src.camion import Camion


class TestVehiculo(unittest.TestCase):
    """Casos de prueba para el ciclo de vida y operaciones de Vehiculo."""

    def setUp(self) -> None:
        """Inicializa una instancia limpia de Vehiculo antes de cada prueba."""
        self.vehiculo = Vehiculo(patente="ABC123", anio=2020)

    def test_inicializacion_valida(self) -> None:
        """Verifica la asignación correcta de atributos iniciales."""
        self.assertEqual(self.vehiculo.patente, "ABC123")
        self.assertEqual(self.vehiculo.anio, 2020)
        self.assertFalse(self.vehiculo.en_taller)

    def test_setter_patente_valida(self) -> None:
        """Verifica que se pueda actualizar la patente con un valor válido."""
        self.vehiculo.patente = "XYZ789"
        self.assertEqual(self.vehiculo.patente, "XYZ789")

    def test_setter_patente_invalida_largo(self) -> None:
        """Verifica que patente con menos de 6 caracteres lance ValueError."""
        with self.assertRaises(ValueError):
            Vehiculo(patente="AB12", anio=2020)

    def test_setter_patente_invalida_espacios(self) -> None:
        """Verifica que patente con espacios lance ValueError."""
        with self.assertRaises(ValueError):
            self.vehiculo.patente = "AB 1234"

    def test_en_taller_solo_lectura(self) -> None:
        """Verifica que en_taller no permita asignación directa."""
        with self.assertRaises(AttributeError):
            self.vehiculo.en_taller = True

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

    def test_polimorfismo_tarifas(self) -> None:
        """Verifica que cada clase retorne su tarifa por hora correspondiente."""
        auto = Auto(patente="AUTO12", anio=2021)
        moto = Moto(patente="MOTO34", anio=2022)
        camion = Camion(patente="CAMI56", anio=2019, capacidad_carga=4000)

        self.assertEqual(self.vehiculo.tarifa_hora(), 5000)
        self.assertEqual(auto.tarifa_hora(), 25000)
        self.assertEqual(moto.tarifa_hora(), 15000)
        self.assertEqual(camion.tarifa_hora(), 40000)


if __name__ == "__main__":
    unittest.main()
