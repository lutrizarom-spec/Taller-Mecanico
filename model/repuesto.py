class Repuesto:  # Define la entidad Repuesto para la gestión de piezas y repuestos del taller

    def __init__(self, id_repuesto: int, nombre: str, precio: float, stock: int, descripcion: str = ""):
        self.id_repuesto = id_repuesto  # Identificador único correlativo del repuesto
        self.nombre = nombre  # Nombre comercial del repuesto (ej: 'Filtro de Aceite')
        self.precio = precio  # Valor unitario monetario del repuesto
        self.stock = stock  # Cantidad física disponible en bodega
        self.descripcion = descripcion  # Detalles técnicos o compatibilidad de la pieza
