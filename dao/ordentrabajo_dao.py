from conectar import obtener_conexion  # Importa la función de conexión a BD
from model.ordentrabajo import OrdenTrabajo  # Importa la entidad OrdenTrabajo
from dao.dao import BaseDAO  # Importa la interfaz abstracta base


class OrdenTrabajoDAO(BaseDAO):  # Implementación DAO para administrar Órdenes de Trabajo

    def crear(self, orden: OrdenTrabajo):  # Inserta una nueva orden de trabajo en la BD
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute(  # Ejecuta inserción con FKs de cliente, vehículo y usuario
                "INSERT INTO ordenes_trabajo (id_orden, rut_cliente, patente_vehiculo, id_usuario, estado, fecha_ingreso) VALUES (?, ?, ?, ?, ?, ?)",
                (orden.id_orden, orden.rut_cliente, orden.patente_vehiculo, orden.id_usuario, orden.estado, orden.fecha_ingreso)
            )
            conn.commit()  # Confirma la transacción en BD

    def obtener_por_id(self, id_orden: int):  # Búsqueda por número único de orden
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT id_orden, rut_cliente, patente_vehiculo, id_usuario, estado, fecha_ingreso FROM ordenes_trabajo WHERE id_orden = ?", (id_orden,))  # Consulta filtrada
            row = cursor.fetchone()  # Recupera el registro
            return OrdenTrabajo(row["id_orden"], row["rut_cliente"], row["patente_vehiculo"], row["id_usuario"], row["estado"], row["fecha_ingreso"]) if row else None  # Convierte a objeto

    def listar_todos(self):  # Obtiene todas las órdenes de trabajo registradas
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT id_orden, rut_cliente, patente_vehiculo, id_usuario, estado, fecha_ingreso FROM ordenes_trabajo")  # Consulta SQL masiva
            return [OrdenTrabajo(r["id_orden"], r["rut_cliente"], r["patente_vehiculo"], r["id_usuario"], r["estado"], r["fecha_ingreso"]) for r in cursor.fetchall()]  # Mapea a lista

    def eliminar(self, id_orden: int):  # Elimina una orden por su ID
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("DELETE FROM ordenes_trabajo WHERE id_orden = ?", (id_orden,))  # Ejecuta la eliminación
            conn.commit()  # Confirma borrado
