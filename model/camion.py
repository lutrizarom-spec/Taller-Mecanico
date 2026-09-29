from model.vehiculo import Vehiculo  # Importa la superclase Vehiculo desde model.vehiculo


class Camion(Vehiculo):  # Subclase Camion que hereda de Vehiculo (Fusionado del repo de referencia)

    def __init__(self, patente: str, marca: str, modelo: str, anio: int, capacidad_ton: float = 5.0, en_taller: bool = True):
        super().__init__(patente, marca, modelo, anio, en_taller)  # Inicializa la superclase Vehiculo
        self.capacidad_ton = capacidad_ton  # Capacidad máxima de carga en toneladas (atributo propio de camiones)

    def tarifa_hora(self) -> float:  # Sobrescribe la tarifa_hora aplicando Polimorfismo
        return 12000.0  # Tarifa por hora especializada para vehículos de carga pesada
