"""
Excepciones personalizadas de dominio para el Taller Mecánico.
"""


class TallerError(Exception):
    """Clase base para todas las excepciones del taller mecánico."""
    pass


class StockInsuficienteError(TallerError):
    """Se lanza cuando se intenta usar o reservar más repuestos de los disponibles."""
    def __init__(self, mensaje: str, disponible: int = 0, solicitado: int = 0):
        super().__init__(mensaje)
        self.disponible = disponible
        self.solicitado = solicitado


class DeudaPendienteError(TallerError):
    """Se lanza cuando un usuario con saldo deudor intenta retirar un vehículo o solicitar servicios."""
    def __init__(self, mensaje: str, deuda: int = 0):
        super().__init__(mensaje)
        self.deuda = deuda
