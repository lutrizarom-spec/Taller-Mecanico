from src.vehiculo import Vehiculo  # Importa la clase padre Vehiculo


class Camion(Vehiculo):  # Define la clase hija Camion que hereda de Vehiculo
    """Clase Camion que especializa atributos de carga y tarifa horaria."""

    def __init__(self, patente: str, anio: int, capacidad_carga: int):  # Constructor con atributo propio
        super().__init__(patente, anio)  # Invoca constructor de la clase padre
        self.__capacidad_carga: int = capacidad_carga  # Asigna atributo privado de capacidad en kg

    def tarifa_hora(self) -> int:  # Sobrescribe el método de la clase padre
        return 40000  # Retorna tarifa específica para camiones ($40.000)
