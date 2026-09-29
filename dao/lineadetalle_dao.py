from conectar import obtener_conexion  # Importa el gestor de conexiones
from model.lineadetalle import LineaDetalle  # Importa la entidad LineaDetalle
from dao.dao import BaseDAO  # Importa la interfaz BaseDAO


class LineaDetalleDAO(BaseDAO):  # Implementación DAO para los detalles de repuestos de cada orden

    def crear(self, detalle: LineaDetalle):  # Guarda un detalle de repuesto asociado a una orden
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute(  # Ejecuta inserción con id_orden e id_repuesto
                "INSERT INTO linea_detalle (id_detalle, id_orden, id_repuesto, cantidad, precio_unitario) VALUES (?, ?, ?, ?, ?)",
                (detalle.id_detalle, detalle.id_orden, detalle.id_repuesto, detalle.cantidad, detalle.precio_unitario)
            )
            conn.commit()  # Confirma la transacción

    def obtener_por_id(self, id_detalle: int):  # Busca un ítem de detalle por su ID
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT id_detalle, id_orden, id_repuesto, cantidad, precio_unitario FROM linea_detalle WHERE id_detalle = ?", (id_detalle,))  # Consulta SQL
            row = cursor.fetchone()  # Recupera fila
            return LineaDetalle(row["id_detalle"], row["id_orden"], row["id_repuesto"], row["cantidad"], row["precio_unitario"]) if row else None  # Mapea a objeto

    def listar_todos(self):  # Obtiene la lista completa de detalles
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT id_detalle, id_orden, id_repuesto, cantidad, precio_unitario FROM linea_detalle")  # Consulta masiva
            return [LineaDetalle(r["id_detalle"], r["id_orden"], r["id_repuesto"], r["cantidad"], r["precio_unitario"]) for r in cursor.fetchall()]  # Retorna lista

    def eliminar(self, id_detalle: int):  # Elimina un detalle por su ID
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("DELETE FROM linea_detalle WHERE id_detalle = ?", (id_detalle,))  # Borra el registro
            conn.commit()  # Confirma borrado
