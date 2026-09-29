class LineaDetalle:  # Entidad de relación que desglose las piezas consumidas en una Orden de Trabajo

    def __init__(self, id_detalle: int, id_orden: int, id_repuesto: int, cantidad: int, precio_unitario: float):
        self.id_detalle = id_detalle  # Clave primaria única de la línea de detalle
        self.id_orden = id_orden  # Clave foránea que asocia este ítem con una OrdenTrabajo
        self.id_repuesto = id_repuesto  # Clave foránea que vincula el Repuesto utilizado
        self.cantidad = cantidad  # Unidades utilizadas del repuesto
        self.precio_unitario = precio_unitario  # Precio al momento de generar el detalle

    def subtotal(self) -> float:  # Cálculo dinámico del monto parcial
        return self.cantidad * self.precio_unitario  # Multiplica la cantidad consumida por el precio unitario
