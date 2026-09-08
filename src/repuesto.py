from src.excepciones import StockInsuficienteError


class Repuesto:
    """Modela una pieza o insumo de taller que cuenta con stock finito y control de agotamiento."""

    def __init__(self, codigo: str, nombre: str, precio: int, stock: int = 0):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def codigo(self) -> str:
        return self.__codigo

    @codigo.setter
    def codigo(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El código del repuesto no puede estar vacío.")
        self.__codigo = valor.strip().upper()

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del repuesto no puede estar vacío.")
        self.__nombre = valor.strip()

    @property
    def precio(self) -> int:
        return self.__precio

    @precio.setter
    def precio(self, valor: int) -> None:
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El precio del repuesto debe ser un número positivo mayor a 0.")
        self.__precio = int(valor)

    @property
    def stock(self) -> int:
        return self.__stock

    @stock.setter
    def stock(self, valor: int) -> None:
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("El stock no puede ser negativo ni contener decimales.")
        self.__stock = valor

    def usar(self, cantidad: int) -> None:
        """Descuenta unidades de stock del repuesto. Lanza StockInsuficienteError si no alcanza."""
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad a usar debe ser un entero positivo mayor a 0.")
        if cantidad > self.__stock:
            raise StockInsuficienteError(
                f"Stock insuficiente para '{self.__nombre}'. Solicitado: {cantidad}, Disponible: {self.__stock}.",
                disponible=self.__stock,
                solicitado=cantidad,
            )
        self.__stock -= cantidad

    def reponer(self, cantidad: int) -> None:
        """Incrementa el stock con nuevas unidades recibidas."""
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad a reponer debe ser un entero positivo mayor a 0.")
        self.__stock += cantidad

    def __str__(self) -> str:
        return f"Repuesto [{self.__codigo}] {self.__nombre} - Stock: {self.__stock} u. - Precio: ${self.__precio:,}"
