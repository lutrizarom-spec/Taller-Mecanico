class Marca:  # Clase de dominio que representa una marca de vehículo

    def __init__(self, id_marca: int, nombre: str):
        self.id_marca = id_marca  # Clave primaria numérica de la marca
        self.nombre = nombre  # Nombre comercial de la marca (ej: Toyota)
