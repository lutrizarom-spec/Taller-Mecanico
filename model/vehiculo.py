class Vehiculo:  # Superclase base para la jerarquía de vehículos en el taller

    def __init__(self, patente: str, marca: str, modelo: str, anio: int, en_taller: bool = True):
        self.patente = patente  # Identificador único oficial del vehículo (Placa / Patente)
        self.marca = marca  # Marca asociada al vehículo
        self.modelo = modelo  # Modelo asociado al vehículo
        self.anio = anio  # Año de fabricación del vehículo
        self.en_taller = en_taller  # Estado operativo: True si está ingresado en el taller, False si fue entregado

    def tarifa_hora(self) -> float:  # Método genérico para calcular tarifa por hora de trabajo
        return 5000.0  # Tarifa base general predeterminada para mantenimiento
