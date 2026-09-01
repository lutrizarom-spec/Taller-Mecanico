from src.vehiculo import Vehiculo  # Importa la clase padre Vehiculo


class Moto(Vehiculo):  # Define la clase hija Moto que hereda de Vehiculo
    """Clase Moto que especializa la tarifa horaria para motocicletas."""

    def tarifa_hora(self) -> int:  # Sobrescribe el método de la clase padre
        return 15000  # Retorna tarifa específica para motos ($15.000)
