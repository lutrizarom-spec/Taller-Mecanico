from model.vehiculo import Vehiculo  # Importa la clase padre Vehiculo


class Auto(Vehiculo):  # Subclase Auto que hereda las propiedades generales de Vehiculo

    def __init__(self, patente: str, marca: str, modelo: str, anio: int, num_puertas: int = 4, en_taller: bool = True):
        super().__init__(patente, marca, modelo, anio, en_taller)  # Inicializa la superclase Vehiculo
        self.num_puertas = num_puertas  # Propiedad específica de autos: número de puertas (ej: 3, 4, 5)

    def tarifa_hora(self) -> float:  # Sobrescribe el método de la superclase (Polimorfismo)
        return 6500.0  # Tarifa por hora específica diferenciada para automóviles
