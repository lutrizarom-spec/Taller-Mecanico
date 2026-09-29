from model.vehiculo import Vehiculo  # Importa la superclase Vehiculo desde el paquete model


class Moto(Vehiculo):  # Subclase Moto que extiende a Vehiculo (Fusionado del repositorio de referencia)

    def __init__(self, patente: str, marca: str, modelo: str, anio: int, cilindrada: int = 150, en_taller: bool = True):
        super().__init__(patente, marca, modelo, anio, en_taller)  # Hereda los atributos básicos de vehiculo
        self.cilindrada = cilindrada  # Cilindrada en cc (atributo exclusivo de motocicletas)

    def tarifa_hora(self) -> float:  # Sobrescribe la tarifa por hora usando Polimorfismo
        return 4500.0  # Tarifa diferenciada por hora para mantenimiento de motocicletas
