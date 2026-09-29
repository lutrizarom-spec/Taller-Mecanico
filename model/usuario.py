from model.persona import Persona  # Importa la superclase Persona


class Usuario(Persona):  # Declara Usuario extendiendo las capacidades de Persona

    def __init__(self, rut: str, nombre: str, apellido: str, telefono: str = "", email: str = "", username: str = "", clave: str = "", id_rol: int = 1):
        super().__init__(rut, nombre, apellido, telefono, email)  # Hereda datos básicos de identidad
        self.username = username  # Nombre de cuenta para autenticación en el sistema
        self.clave = clave  # Contraseña de acceso (almacenada/encriptada)
        self.id_rol = id_rol  # Clave foránea que vincula este usuario con un Rol específico
