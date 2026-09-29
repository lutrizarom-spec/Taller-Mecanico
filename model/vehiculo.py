class Vehiculo:  # Clase base para la entidad Vehículo

    def __init__(self, patente: str, marca: str, modelo: str, anio: int):
        self.patente = patente  # Identificador único de la placa del vehículo
        self.marca = marca  # Nombre o referencia de la marca
        self.modelo = modelo  # Nombre o referencia del modelo
        self.anio = anio  # Año de fabricación del vehículo
