class Modelo:  # Representa un modelo específico de vehículo asociado a una Marca

    def __init__(self, id_modelo: int, id_marca: int, nombre: str):
        self.id_modelo = id_modelo  # Clave primaria única del modelo
        self.id_marca = id_marca  # Clave foránea que relaciona el modelo con su Marca correspondiente
        self.nombre = nombre  # Nombre comercial del modelo (ej: Corolla, Yaris, Aveo)
