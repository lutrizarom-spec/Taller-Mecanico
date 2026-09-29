from model.vehiculo import Vehiculo  # Importa la clase base Vehiculo desde model


class Auto(Vehiculo):  # Clase Auto que hereda atributos y métodos de Vehiculo

    def __init__(self, patente: str, marca: str, modelo: str, anio: int, num_puertas: int = 4):
        super().__init__(patente, marca, modelo, anio)  # Inicializa los atributos heredados
        self.num_puertas = num_puertas  # Cantidad de puertas del vehículo
