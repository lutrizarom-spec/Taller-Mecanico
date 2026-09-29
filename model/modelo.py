class Modelo:  # Clase de dominio que representa un modelo asociado a una marca

    def __init__(self, id_modelo: int, id_marca: int, nombre: str):
        self.id_modelo = id_modelo  # Clave primaria numérica del modelo
        self.id_marca = id_marca  # Clave foránea referenciando a la marca
        self.nombre = nombre  # Nombre comercial del modelo (ej: Corolla)
