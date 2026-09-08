"""
Suite de Pruebas Unitarias para Vehiculo y Clases Hijas.
"""

import unittest
from src.vehiculo import Vehiculo
from src.auto import Auto
from src.moto import Moto
from src.camion import Camion, TipoCamion


class VehiculoConcreto(Vehiculo):
    """Subclase concreta auxiliar para probar métodos heredados de la clase abstracta Vehiculo."""
    def tarifa_hora(self) -> int:
        return 5000


class TestVehiculo(unittest.TestCase):
    """Casos de prueba para el ciclo de vida y operaciones de Vehiculo."""

    def setUp(self) -> None:
        """Inicializa una instancia limpia de subclase concreta antes de cada prueba."""
        self.vehiculo = VehiculoConcreto(patente="AB1234", anio=2020)

    def test_vehiculo_es_clase_abstracta(self) -> None:
        """Verifica que Vehiculo no se pueda instanciar directamente por ser una clase abstracta."""
        with self.assertRaises(TypeError):
            Vehiculo(patente="AB1234", anio=2020)  # type: ignore

    def test_inicializacion_valida(self) -> None:
        """Verifica la asignación correcta de atributos iniciales."""
        self.assertEqual(self.vehiculo.patente, "AB1234")
        self.assertEqual(self.vehiculo.anio, 2020)
        self.assertFalse(self.vehiculo.en_taller)

    def test_setter_patente_valida(self) -> None:
        """Verifica que se pueda actualizar la patente con un valor válido en ambos formatos chilenos."""
        self.vehiculo.patente = "BBCC12"  # Formato nuevo: 4 letras y 2 números
        self.assertEqual(self.vehiculo.patente, "BBCC12")
        self.vehiculo.patente = "cd5678"  # Formato antiguo en minúscula normalizado
        self.assertEqual(self.vehiculo.patente, "CD5678")

    def test_setter_patente_invalida_largo(self) -> None:
        """Verifica que patente con menos de 6 caracteres lance ValueError."""
        with self.assertRaises(ValueError):
            Auto(patente="AB12", anio=2020)

    def test_setter_patente_invalida_espacios(self) -> None:
        """Verifica que patente con espacios lance ValueError."""
        with self.assertRaises(ValueError):
            self.vehiculo.patente = "AB 1234"

    def test_setter_patente_invalida_formato(self) -> None:
        """Verifica que combinaciones fuera de formato chileno lancen ValueError."""
        with self.assertRaises(ValueError):
            self.vehiculo.patente = "ABC123"  # 3 letras y 3 números inválido

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

    def test_tarifas_tipo_camion(self) -> None:
        """Verifica las tarifas según el tipo de camión y sus recargos."""
        rampla = Camion(patente="RAMP12", anio=2020, capacidad_carga=5000, tipo=TipoCamion.RAMPLA_NORMAL)
        doble = Camion(patente="DOBL34", anio=2021, capacidad_carga=8000, tipo=TipoCamion.DOBLE_RAMPLA)
        explosivos = Camion(patente="EXPL56", anio=2022, capacidad_carga=3000, tipo=TipoCamion.TRANSPORTE_EXPLOSIVOS)

        self.assertEqual(rampla.tarifa_hora(), 40000)
        self.assertEqual(doble.tarifa_hora(), 50000)
        self.assertEqual(explosivos.tarifa_hora(), 60000)

    def test_validaciones_camion(self) -> None:
        """Verifica validación de capacidad positiva y tipo válido en Camion."""
        with self.assertRaises(ValueError):
            Camion(patente="CAMI11", anio=2020, capacidad_carga=-100)
        with self.assertRaises(ValueError):
            Camion(patente="CAMI22", anio=2020, capacidad_carga=5000, tipo="TipoInexistente")


if __name__ == "__main__":
    unittest.main()
