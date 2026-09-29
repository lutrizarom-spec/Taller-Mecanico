from conectar import obtener_conexion  # Importa la función de conexión central
from model.marca import Marca  # Importa la entidad Marca
from dao.dao import BaseDAO  # Importa la interfaz BaseDAO


class MarcaDAO(BaseDAO):  # Implementación DAO concreta para el catálogo de Marcas

    def crear(self, marca: Marca):  # Guarda una nueva marca comercial en la BD
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("INSERT INTO marcas (nombre) VALUES (?)", (marca.nombre,))  # Ejecuta la inserción SQL
            conn.commit()  # Guarda los cambios

    def obtener_por_id(self, id_marca: int):  # Busca una marca por su clave primaria
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT id_marca, nombre FROM marcas WHERE id_marca = ?", (id_marca,))  # Consulta filtrada
            row = cursor.fetchone()  # Recupera el registro
            return Marca(row["id_marca"], row["nombre"]) if row else None  # Retorna objeto Marca o None

    def listar_todos(self):  # Obtiene el listado completo de marcas
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT id_marca, nombre FROM marcas")  # Consulta SQL
            return [Marca(r["id_marca"], r["nombre"]) for r in cursor.fetchall()]  # Mapea a lista de objetos Marca

    def eliminar(self, id_marca: int):  # Elimina una marca registrada
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("DELETE FROM marcas WHERE id_marca = ?", (id_marca,))  # Ejecuta la eliminación
            conn.commit()  # Guarda el estado
