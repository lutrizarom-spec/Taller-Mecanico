from datetime import datetime  # Importa la librería estándar para la gestión de fechas


class OrdenTrabajo:  # Entidad del modelo que coordina las reparaciones y servicios en el taller

    def __init__(self, id_orden: int, rut_cliente: str, patente_vehiculo: str, id_usuario: int, estado: str = "Ingresado", fecha_ingreso: str = None):
        self.id_orden = id_orden  # Clave primaria autoincremental de la orden de trabajo
        self.rut_cliente = rut_cliente  # Clave foránea que referencia al Cliente que solicita el servicio
        self.patente_vehiculo = patente_vehiculo  # Clave foránea que vincula el Vehículo a reparar
        self.id_usuario = id_usuario  # Clave foránea que identifica al operador/mecánico a cargo
        self.estado = estado  # Estado del ciclo de vida (ej: 'Ingresado', 'En Proceso', 'Finalizado')
        self.fecha_ingreso = fecha_ingreso if fecha_ingreso else datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Fecha y hora de creación
