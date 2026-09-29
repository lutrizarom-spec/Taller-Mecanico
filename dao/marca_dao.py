from conectar import obtener_conexion  # Importa la conexión central a la BD
from model.marca import Marca  # Importa el modelo Marca
from dao.dao import BaseDAO  # Importa la interfaz DAO base


class MarcaDAO(BaseDAO):  # Implementación DAO para la entidad Marca

    def crear(self, marca: Marca):  # Inserta una marca en la BD
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("INSERT INTO marcas (nombre) VALUES (?)", (marca.nombre,))  # Inserción parametrizada
            conn.commit()  # Guarda los cambios

    def obtener_por_id(self, id_marca: int):  # Busca marca por ID
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT id_marca, nombre FROM marcas WHERE id_marca = ?", (id_marca,))  # Consulta por ID
            row = cursor.fetchone()  # Obtiene la fila
            return Marca(row["id_marca"], row["nombre"]) if row else None  # Retorna objeto o None

    def listar_todos(self):  # Lista todas las marcas
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT id_marca, nombre FROM marcas")  # Obtiene registros
            return [Marca(r["id_marca"], r["nombre"]) for r in cursor.fetchall()]  # Retorna lista

    def eliminar(self, id_marca: int):  # Elimina una marca por ID
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("DELETE FROM marcas WHERE id_marca = ?", (id_marca,))  # Elimina registro
            conn.commit()  # Guarda cambios
