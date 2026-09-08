import unittest
from src.repuesto import Repuesto
from src.excepciones import StockInsuficienteError


class TestRepuesto(unittest.TestCase):
    """Casos de prueba para la gestión de inventario y stock en Repuesto."""

    def setUp(self) -> None:
        self.repuesto = Repuesto(codigo="FILT-01", nombre="Filtro de Aceite", precio=8500, stock=5)

    def test_creacion_valida(self) -> None:
        self.assertEqual(self.repuesto.codigo, "FILT-01")
        self.assertEqual(self.repuesto.nombre, "Filtro de Aceite")
        self.assertEqual(self.repuesto.precio, 8500)
        self.assertEqual(self.repuesto.stock, 5)

    def test_usar_stock_valido(self) -> None:
        self.repuesto.usar(2)
        self.assertEqual(self.repuesto.stock, 3)

    def test_usar_stock_exacto(self) -> None:
        self.repuesto.usar(5)
        self.assertEqual(self.repuesto.stock, 0)

    def test_usar_stock_insuficiente_lanza_excepcion(self) -> None:
        with self.assertRaises(StockInsuficienteError) as ctx:
            self.repuesto.usar(6)

        self.assertEqual(ctx.exception.disponible, 5)
        self.assertEqual(ctx.exception.solicitado, 6)
        self.assertIn("Stock insuficiente", str(ctx.exception))
        # El stock no debe alterarse tras la falla
        self.assertEqual(self.repuesto.stock, 5)

    def test_reponer_stock(self) -> None:
        self.repuesto.reponer(10)
        self.assertEqual(self.repuesto.stock, 15)

    def test_validaciones_invalido(self) -> None:
        with self.assertRaises(ValueError):
            Repuesto(codigo="", nombre="Batería", precio=50000, stock=2)

        with self.assertRaises(ValueError):
            Repuesto(codigo="BAT-01", nombre="Batería", precio=-1000, stock=2)

        with self.assertRaises(ValueError):
            Repuesto(codigo="BAT-01", nombre="Batería", precio=50000, stock=-1)

        with self.assertRaises(ValueError):
            self.repuesto.usar(0)

        with self.assertRaises(ValueError):
            self.repuesto.reponer(-5)


if __name__ == "__main__":
    unittest.main()
