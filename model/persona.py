class Persona:  # Define la superclase abstracta/base para representar a cualquier persona en el sistema

    def __init__(self, rut: str, nombre: str, apellido: str, telefono: str = "", email: str = ""):
        self.rut = rut  # Identificador único oficial (Clave primaria conceptual)
        self.nombre = nombre  # Primer nombre de la persona
        self.apellido = apellido  # Apellidos paterno y materno
        self.telefono = telefono  # Teléfono de contacto (Opcional, por defecto cadena vacía)
        self.email = email  # Correo electrónico institucional o personal (Opcional)

    def nombre_completo(self) -> str:  # Método helper para obtener el nombre formateado
        return f"{self.nombre} {self.apellido}"  # Retorna el nombre y apellido concatenados con espacio
