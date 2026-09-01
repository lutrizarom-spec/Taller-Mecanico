class Vehiculo:  # Define la clase Vehiculo
    def __init__(self, patente: str, anio: int):  # Constructor que recibe patente y año al crear el objeto
        self.__patente: str = patente  # Asigna la patente recibida a un atributo privado
        self.__anio: int = anio  # Asigna el año recibido a un atributo privado
        self.__en_taller: bool = False  # Inicializa el estado en False (no está en el taller por defecto) como privado

    @property
    def patente(self) -> str:  # Getter para acceder a la patente de forma segura
        return self.__patente  # Retorna la patente del vehículo

    @property
    def anio(self) -> int:  # Getter para acceder al año de fabricación
        return self.__anio  # Retorna el año del vehículo

    @property
    def en_taller(self) -> bool:  # Getter para consultar si el vehículo está en el taller
        return self.__en_taller  # Retorna True si está en el taller, False si no

    def ingresar(self) -> str:  # Método para registrar el ingreso del vehículo al taller
        if self.__en_taller:  # Verifica si el vehículo ya está marcado como dentro del taller
            return "El vehículo ya se encuentra en el taller."  # Devuelve mensaje si ya estaba ingresado
        self.__en_taller = True  # Cambia el estado a True (ingresado)
        return "El vehículo ha ingresado al taller."  # Devuelve mensaje de éxito

    def entregar(self) -> str:  # Método para registrar la salida o entrega del vehículo
        if not self.__en_taller:  # Verifica si el vehículo no está en el taller
            return "El vehículo no se encuentra en el taller."  # Devuelve mensaje indicando que no se puede entregar
        self.__en_taller = False  # Cambia el estado a False (fuera del taller)
        return "El vehículo ha sido entregado."  # Devuelve mensaje de éxito

    def tarifa_hora(self) -> int:  # Método que retorna el costo de la tarifa por hora
        return 5000  # Retorna un valor fijo de 5000

    def __str__(self) -> str:  # Representación textual del vehículo
        estado = "En Taller" if self.__en_taller else "Disponible / Fuera de Taller"  # Determina etiqueta de estado
        return f"Vehículo [Patente: {self.__patente}, Año: {self.__anio}, Estado: {estado}]"  # Retorna resumen legible
