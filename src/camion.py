from enum import Enum
from src.vehiculo import Vehiculo


class TipoCamion(Enum):
    """Enumeración con los tipos especializados de camión admitidos en el taller."""
    RAMPLA_NORMAL = "Rampla Normal"
    DOBLE_RAMPLA = "Doble Rampla"
    TRANSPORTE_EXPLOSIVOS = "Transporte Explosivos"


class Camion(Vehiculo):
    """Clase Camion que especializa atributos de carga, tipo operativo y tarifa horaria."""

    def __init__(
        self,
        patente: str,
        anio: int,
        capacidad_carga: int,
        tipo: TipoCamion = TipoCamion.RAMPLA_NORMAL,
    ):
        super().__init__(patente, anio)
        self.capacidad_carga = capacidad_carga  # Ejecuta validación en setter
        self.tipo = tipo  # Ejecuta validación en setter

    @property
    def capacidad_carga(self) -> int:
        """Getter para acceder a la capacidad de carga en kilogramos."""
        return self.__capacidad_carga

    @capacidad_carga.setter
    def capacidad_carga(self, valor: int) -> None:
        """Valida que la capacidad de carga sea un valor positivo mayor a 0."""
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("La capacidad de carga debe ser un número positivo mayor a 0.")
        self.__capacidad_carga = int(valor)

    @property
    def tipo(self) -> TipoCamion:
        """Getter para acceder al tipo de camión."""
        return self.__tipo

    @tipo.setter
    def tipo(self, valor: TipoCamion) -> None:
        """Valida y asigna el tipo de camión asegurando pertenencia a TipoCamion."""
        if isinstance(valor, TipoCamion):
            self.__tipo = valor
        elif isinstance(valor, str):
            for item in TipoCamion:
                if item.value.lower() == valor.lower() or item.name.lower() == valor.lower():
                    self.__tipo = item
                    return
            raise ValueError(f"Tipo de camión '{valor}' no válido. Opciones permitidas: {[t.value for t in TipoCamion]}")
        else:
            raise ValueError("El tipo de camión debe ser una instancia de TipoCamion o texto válido.")

    def tarifa_hora(self) -> int:
        """Calcula tarifa horaria con recargo según la criticidad del tipo de camión."""
        tarifa_base = 40000
        if self.__tipo == TipoCamion.TRANSPORTE_EXPLOSIVOS:
            return int(tarifa_base * 1.50)  # +50% ($60.000)
        elif self.__tipo == TipoCamion.DOBLE_RAMPLA:
            return int(tarifa_base * 1.25)  # +25% ($50.000)
        return tarifa_base  # Rampla normal ($40.000)
