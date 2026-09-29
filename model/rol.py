class Rol:  # Define la entidad Rol para gestionar niveles de acceso del sistema (Fusionado desde el repositorio de referencia)

    def __init__(self, id_rol: int, nombre_rol: str, descripcion: str = ""):
        self.id_rol = id_rol  # Clave primaria numérica de autoincremento en BD
        self.nombre_rol = nombre_rol  # Nombre del rol (ej: 'Administrador', 'Mecánico', 'Recepcionista')
        self.descripcion = descripcion  # Explicación del alcance y permisos asignados al rol
