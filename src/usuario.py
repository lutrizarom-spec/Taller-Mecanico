from src.excepciones import DeudaPendienteError
from src.vehiculo import Vehiculo


class Usuario:
    """Modela a un usuario/cliente del taller con control de saldo deudor."""

    def __init__(self, rut: str, nombre: str, deuda: int = 0):
        self.rut = rut
        self.nombre = nombre
        self.deuda = deuda

    @property
    def rut(self) -> str:
        return self.__rut

    @rut.setter
    def rut(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El RUT del usuario no puede estar vacío.")
        self.__rut = valor.strip().upper()

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del usuario no puede estar vacío.")
        self.__nombre = valor.strip()

    @property
    def deuda(self) -> int:
        return self.__deuda

    @deuda.setter
    def deuda(self, valor: int) -> None:
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("La deuda no puede ser un valor negativo.")
        self.__deuda = int(valor)

    def registrar_deuda(self, monto: int) -> None:
        """Suma un cargo impago a la cuenta del usuario."""
        if not isinstance(monto, (int, float)) or monto <= 0:
            raise ValueError("El monto a cargar debe ser positivo.")
        self.__deuda += int(monto)

    def pagar_deuda(self, monto: int) -> int:
        """Abona un monto a la deuda. Retorna el vuelto si el pago excede la deuda."""
        if not isinstance(monto, (int, float)) or monto <= 0:
            raise ValueError("El monto a pagar debe ser positivo.")
        monto_int = int(monto)
        if monto_int >= self.__deuda:
            vuelto = monto_int - self.__deuda
            self.__deuda = 0
            return vuelto
        else:
            self.__deuda -= monto_int
            return 0

    def retirar_vehiculo(self, vehiculo: Vehiculo) -> str:
        """Intenta retirar el vehículo del taller. Bloquea la entrega si existe deuda pendiente."""
        if not isinstance(vehiculo, Vehiculo):
            raise TypeError("El objeto a retirar debe ser una instancia de Vehiculo.")

        if self.__deuda > 0:
            raise DeudaPendienteError(
                f"El usuario '{self.__nombre}' presenta una deuda de ${self.__deuda:,} "
                f"y no está autorizado para retirar el vehículo con patente {vehiculo.patente}.",
                deuda=self.__deuda,
            )

        return vehiculo.entregar()

    def __str__(self) -> str:
        estado_deuda = f"Deuda: ${self.__deuda:,}" if self.__deuda > 0 else "Al día (Sin deuda)"
        return f"Usuario [{self.__rut}] {self.__nombre} - Estado: {estado_deuda}"
