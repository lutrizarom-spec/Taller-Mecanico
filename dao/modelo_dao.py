from conectar import obtener_conexion  # Importa la función de conexión central
from model.modelo import Modelo  # Importa la entidad Modelo
from dao.dao import BaseDAO  # Importa la interfaz BaseDAO


class ModeloDAO(BaseDAO):  # Implementación DAO para el catálogo de Modelos

    def crear(self, modelo: Modelo):  # Guarda un nuevo modelo asociado a una marca
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("INSERT INTO modelos (id_marca, nombre) VALUES (?, ?)", (modelo.id_marca, modelo.nombre))  # Inserción con FK id_marca
            conn.commit()  # Confirma cambios

    def obtener_por_id(self, id_modelo: int):  # Busca un modelo por su ID único
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT id_modelo, id_marca, nombre FROM modelos WHERE id_modelo = ?", (id_modelo,))  # Consulta filtrada
            row = cursor.fetchone()  # Recupera fila
            return Modelo(row["id_modelo"], row["id_marca"], row["nombre"]) if row else None  # Mapea a objeto Modelo o None

    def listar_todos(self):  # Obtiene todos los modelos registrados
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT id_modelo, id_marca, nombre FROM modelos")  # Consulta SQL
            return [Modelo(r["id_modelo"], r["id_marca"], r["nombre"]) for r in cursor.fetchall()]  # Retorna lista de objetos

    def eliminar(self, id_modelo: int):  # Elimina un modelo por su ID
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("DELETE FROM modelos WHERE id_modelo = ?", (id_modelo,))  # Borrado SQL
            conn.commit()  # Confirma la acción
