class Marca:  # Define la clase Marca para representar una marca en el dominio
    def __init__(self, nombre: str, id: int = None):  # Constructor que recibe el nombre y opcionalmente el id
        self.__id = id  # Inicializa el atributo privado id
        self.__nombre = nombre  # Inicializa el atributo privado nombre

    @property
    def id(self) -> int:  # Getter para acceder al atributo privado id
        return self.__id  # Retorna el id de la marca

    @property
    def nombre(self) -> str:  # Getter para acceder al atributo privado nombre
        return self.__nombre  # Retorna el nombre de la marca

    def __repr__(self) -> str:  # Define la representación oficial en cadena del objeto
        return f"Marca(id={self.__id}, nombre='{self.__nombre}')"  # Retorna formato descriptivo del objeto

    def __str__(self) -> str:  # Define la representación en texto legible del objeto
        return f"Marca(id={self.__id}, nombre='{self.__nombre}')"  # Retorna formato descriptivo del objeto
