from model.persona import Persona  # Importa la clase padre Persona desde el paquete model


class Cliente(Persona):  # Clase Cliente que hereda atributos y métodos de Persona

    def __init__(self, rut: str, nombre: str, apellido: str, telefono: str = "", email: str = "", direccion: str = ""):
        super().__init__(rut, nombre, apellido, telefono, email)  # Llama al constructor de Persona
        self.direccion = direccion  # Dirección física particular del cliente
