import sqlite3  # Importa la librería oficial de SQLite en Python

DB_NAME = "taller.db"  # Nombre del archivo SQLite que actúa como almacenamiento relacional


def obtener_conexion():  # Función centralizada para entregar conexiones configuradas
    conexion = sqlite3.connect(DB_NAME)  # Abre la conexión con la base de datos local
    conexion.row_factory = sqlite3.Row  # Configura la devolución de consultas como diccionarios mapeados
    conexion.execute("PRAGMA foreign_keys = ON;")  # Fuerza la verificación estricta de restricciones relacionales
    return conexion  # Retorna el objeto conexión listo para trabajar con bloques 'with'
