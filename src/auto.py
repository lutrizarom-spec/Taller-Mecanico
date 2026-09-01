from src.vehiculo import Vehiculo  # Importa la clase padre Vehiculo


class Auto(Vehiculo):  # Define la clase hija Auto que hereda de Vehiculo
    """Clase Auto que especializa la tarifa horaria para automóviles."""

    def tarifa_hora(self) -> int:  # Sobrescribe el método de la clase padre
        return 25000  # Retorna tarifa específica para autos ($25.000)
