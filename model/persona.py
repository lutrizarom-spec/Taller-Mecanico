class Persona:  # Clase base para representar entidades con datos personales

    def __init__(self, rut: str, nombre: str, apellido: str, telefono: str = "", email: str = ""):
        self.rut = rut  # Identificador único de la persona (RUT)
        self.nombre = nombre  # Primer nombre de la persona
        self.apellido = apellido  # Apellido de la persona
        self.telefono = telefono  # Número telefónico de contacto
        self.email = email  # Correo electrónico de contacto

    def nombre_completo(self) -> str:  # Método auxiliar para obtener el nombre completo
        return f"{self.nombre} {self.apellido}"  # Concatena nombre y apellido
