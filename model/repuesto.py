class StockInsuficienteError(Exception):
    """Excepción personalizada para manejo de stock insuficiente."""
    pass

class Repuesto:
    """
    Gestión de repuestos del taller.
    Soluciona la falla silenciosa mediante el lanzamiento explícito de StockInsuficienteError.
    """
    def __init__(self, nombre: str, precio: int, stock: int, id: int = None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, valor: int):
        self.__id = valor

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or len(valor.strip()) == 0:
            raise ValueError("El nombre del repuesto no puede estar vacío.")
        self.__nombre = valor.strip()

    @property
    def precio(self) -> int:
        return self.__precio

    @precio.setter
    def precio(self, valor: int):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.__precio = valor

    @property
    def stock(self) -> int:
        return self.__stock

    @stock.setter
    def stock(self, valor: int):
        if valor < 0:
            raise ValueError("El stock no puede ser negativo.")
        self.__stock = valor

    def aumentar_stock(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0.")
        self.stock += cantidad

    def disminuir_stock(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0.")
        if cantidad > self.stock:
            raise StockInsuficienteError(
                f"Stock insuficiente para '{self.nombre}'. Disponible: {self.stock}, Solicitado: {cantidad}"
            )
        self.stock -= cantidad

    def __str__(self) -> str:
        return f"ID: {self.__id} | Repuesto: {self.__nombre} | Precio: ${self.__precio:,} | Stock: {self.__stock}"