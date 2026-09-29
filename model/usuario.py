from model.persona import Persona  # Importa la clase padre Persona desde el paquete model


class Usuario(Persona):  # Clase Usuario que hereda atributos y métodos de Persona

    def __init__(self, rut: str, nombre: str, apellido: str, telefono: str = "", email: str = "", username: str = "", clave: str = "", rol: str = "operador"):
        super().__init__(rut, nombre, apellido, telefono, email)  # Llama al constructor de la clase base
        self.username = username  # Nombre de usuario para iniciar sesión
        self.clave = clave  # Contraseña de acceso al sistema
        self.rol = rol  # Perfil o nivel de permisos (ej: admin, operador)
