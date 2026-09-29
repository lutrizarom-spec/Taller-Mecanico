import sqlite3

DB_NAME = "taller.db"

def obtener_conexion():
    """
    Establece y retorna una conexión a la base de datos SQLite.
    Activa explícitamente el soporte para claves foráneas (PRAGMA foreign_keys = ON).
    """
    conexion = sqlite3.connect(DB_NAME)
    conexion.row_factory = sqlite3.Row
    conexion.execute("PRAGMA foreign_keys = ON;")
    return conexion
