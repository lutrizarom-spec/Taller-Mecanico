from conectar import obtener_conexion  # Importa la función de conexión a la BD
from model.repuesto import Repuesto  # Importa el modelo Repuesto
from dao.dao import BaseDAO  # Importa la interfaz abstracta base


class RepuestoDAO(BaseDAO):  # Implementación DAO para la gestión de piezas e inventario

    def crear(self, repuesto: Repuesto):  # Inserta un nuevo repuesto en el catálogo
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute(  # Inserción con precio y stock inicial
                "INSERT INTO repuestos (nombre, precio, stock, descripcion) VALUES (?, ?, ?, ?)",
                (repuesto.nombre, repuesto.precio, repuesto.stock, repuesto.descripcion)
            )
            conn.commit()  # Guarda en la BD

    def obtener_por_id(self, id_repuesto: int):  # Busca un repuesto según su ID
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT id_repuesto, nombre, precio, stock, descripcion FROM repuestos WHERE id_repuesto = ?", (id_repuesto,))  # Búsqueda SQL
            row = cursor.fetchone()  # Obtiene resultado
            return Repuesto(row["id_repuesto"], row["nombre"], row["precio"], row["stock"], row["descripcion"]) if row else None  # Instancia objeto

    def listar_todos(self):  # Lista el inventario completo de repuestos
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT id_repuesto, nombre, precio, stock, descripcion FROM repuestos")  # Consulta general
            return [Repuesto(r["id_repuesto"], r["nombre"], r["precio"], r["stock"], r["descripcion"]) for r in cursor.fetchall()]  # Retorna lista

    def eliminar(self, id_repuesto: int):  # Borra un repuesto por su ID
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("DELETE FROM repuestos WHERE id_repuesto = ?", (id_repuesto,))  # Borrado SQL
            conn.commit()  # Confirma borrado
