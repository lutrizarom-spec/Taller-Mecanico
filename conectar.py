import sqlite3  # Importa el módulo nativo sqlite3 para gestionar la base de datos

DB_NAME = "taller.db"  # Nombre del archivo de la base de datos SQLite


def obtener_conexion():  # Función que crea y entrega una conexión configurada
    conexion = sqlite3.connect(DB_NAME)  # Abre la conexión con la BD (se crea si no existe)
    conexion.row_factory = sqlite3.Row  # Permite acceder a las columnas por nombre (ej: fila["nombre"])
    conexion.execute("PRAGMA foreign_keys = ON;")  # Activa la verificación estricta de claves foráneas
    return conexion  # Retorna el objeto de conexión listo para usarse
