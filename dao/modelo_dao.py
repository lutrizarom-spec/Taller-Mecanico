from conectar import obtener_conexion  # Importa la función que establece la conexión a la base de datos SQLite
from model.modelo import Modelo  # Importa la clase de dominio Modelo desde la capa de modelos
from dao.dao import BaseDAO  # Importa la clase base / interfaz abstracta BaseDAO


class ModeloDAO(BaseDAO):  # Define la clase de acceso a datos para Modelo, heredando de BaseDAO

    def crear(self, modelo: Modelo):  # Método para insertar un nuevo modelo en la base de datos
        with obtener_conexion() as conn:  # Abre la conexión usando un bloque 'with' (cierre automático)
            cursor = conn.cursor()  # Crea un objeto cursor para ejecutar consultas SQL
            cursor.execute(  # Ejecuta la sentencia SQL de inserción con parámetros seguros
                "INSERT INTO modelos (id_marca, nombre) VALUES (?, ?)",  # Consulta SQL parametrizada (?)
                (modelo.id_marca, modelo.nombre)  # Tupla con los valores del objeto modelo a insertar
            )
            conn.commit()  # Confirma y guarda los cambios permanentemente en la base de datos

    def obtener_por_id(self, id_modelo: int):  # Método para buscar un modelo por su ID único
        with obtener_conexion() as conn:  # Inicia el contexto de conexión a la BD
            cursor = conn.cursor()  # Obtiene el cursor de ejecución
            cursor.execute(  # Ejecuta la lectura SQL filtrada por clave primaria
                "SELECT id_modelo, id_marca, nombre FROM modelos WHERE id_modelo = ?",  # Sentencia SELECT
                (id_modelo,)  # Tupla con el ID a buscar
            )
            row = cursor.fetchone()  # Recupera la primera fila de los resultados (o None si no existe)
            return Modelo(row["id_modelo"], row["id_marca"], row["nombre"]) if row else None  # Convierte la fila en objeto Modelo o retorna None

    def listar_todos(self):  # Método para obtener la lista de todos los modelos almacenados
        with obtener_conexion() as conn:  # Abre la conexión de manera segura
            cursor = conn.cursor()  # Crea el cursor de la base de datos
            cursor.execute("SELECT id_modelo, id_marca, nombre FROM modelos")  # Consulta que obtiene todos los registros
            return [  # Retorna una lista creada mediante comprensión de listas
                Modelo(r["id_modelo"], r["id_marca"], r["nombre"])  # Instancia un objeto Modelo por cada registro
                for r in cursor.fetchall()  # Recorre todas las filas devueltas por la consulta
            ]

    def eliminar(self, id_modelo: int):  # Método para eliminar un modelo según su ID
        with obtener_conexion() as conn:  # Abre y gestiona el ciclo de vida de la conexión
            cursor = conn.cursor()  # Solicita un nuevo cursor
            cursor.execute("DELETE FROM modelos WHERE id_modelo = ?", (id_modelo,))  # Ejecuta la eliminación del registro
            conn.commit()  # Guarda el cambio de borrado permanentemente en la BD
