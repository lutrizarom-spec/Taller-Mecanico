from conectar import obtener_conexion  # Importa la conexión central a la BD
from model.auto import Auto  # Importa el modelo Auto
from dao.dao import BaseDAO  # Importa la interfaz DAO base


class AutoDAO(BaseDAO):  # Implementación DAO para la entidad Auto

    def crear(self, auto: Auto):  # Inserta un auto en la BD
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("INSERT INTO autos (patente, marca, modelo, anio, num_puertas) VALUES (?, ?, ?, ?, ?)",
                           (auto.patente, auto.marca, auto.modelo, auto.anio, auto.num_puertas))  # Ejecuta inserción con num_puertas
            conn.commit()  # Guarda cambios

    def obtener_por_id(self, patente: str):  # Busca auto por patente
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT patente, marca, modelo, anio, num_puertas FROM autos WHERE patente = ?", (patente,))  # Consulta por patente
            row = cursor.fetchone()  # Recupera fila
            return Auto(row["patente"], row["marca"], row["modelo"], row["anio"], row["num_puertas"]) if row else None  # Retorna objeto Auto o None

    def listar_todos(self):  # Lista todos los autos
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT patente, marca, modelo, anio, num_puertas FROM autos")  # Consulta general
            return [Auto(r["patente"], r["marca"], r["modelo"], r["anio"], r["num_puertas"]) for r in cursor.fetchall()]  # Retorna lista de autos

    def eliminar(self, patente: str):  # Elimina auto por patente
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("DELETE FROM autos WHERE patente = ?", (patente,))  # Elimina registro
            conn.commit()  # Guarda cambios
