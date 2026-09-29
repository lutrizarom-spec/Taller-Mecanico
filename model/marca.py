class Marca:  # Representa la entidad Marca de vehículos en el sistema (ej: Toyota, Chevrolet)

    def __init__(self, id_marca: int, nombre: str):
        self.id_marca = id_marca  # Clave primaria única que identifica la marca
        self.nombre = nombre  # Nombre comercial de la marca de vehículos
