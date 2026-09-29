from model.persona import Persona  # Importa la superclase Persona desde el módulo model.persona


class Cliente(Persona):  # Declara la clase Cliente como subclase de Persona (Aplica Herencia POO)

    def __init__(self, rut: str, nombre: str, apellido: str, telefono: str = "", email: str = "", direccion: str = ""):
        super().__init__(rut, nombre, apellido, telefono, email)  # Reutiliza e inicializa los atributos de Persona
        self.direccion = direccion  # Atributo exclusivo de Cliente para la entrega/facturación de vehículos
