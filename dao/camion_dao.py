from conectar import obtener_conexion  # Importa el gestor de conexiones
from model.camion import Camion  # Importa el modelo Camion
from dao.dao import BaseDAO  # Importa la interfaz BaseDAO


class CamionDAO(BaseDAO):  # Implementación DAO concreta para Camiones de Carga

    def crear(self, camion: Camion):  # Inserta un camión con capacidad de carga en toneladas
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute(  # Inserción con capacidad_ton
                "INSERT INTO camiones (patente, marca, modelo, anio, capacidad_ton, en_taller) VALUES (?, ?, ?, ?, ?, ?)",
                (camion.patente, camion.marca, camion.modelo, camion.anio, camion.capacidad_ton, int(camion.en_taller))
            )
            conn.commit()  # Confirma cambios

    def obtener_por_id(self, patente: str):  # Busca un camión por su patente
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT patente, marca, modelo, anio, capacidad_ton, en_taller FROM camiones WHERE patente = ?", (patente,))  # Búsqueda por patente
            row = cursor.fetchone()  # Recupera fila
            return Camion(row["patente"], row["marca"], row["modelo"], row["anio"], row["capacidad_ton"], bool(row["en_taller"])) if row else None  # Mapea a Camion

    def listar_todos(self):  # Obtiene la lista completa de camiones
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT patente, marca, modelo, anio, capacidad_ton, en_taller FROM camiones")  # Consulta SQL
            return [Camion(r["patente"], r["marca"], r["modelo"], r["anio"], r["capacidad_ton"], bool(r["en_taller"])) for r in cursor.fetchall()]  # Lista de camiones

    def eliminar(self, patente: str):  # Elimina un camión por patente
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("DELETE FROM camiones WHERE patente = ?", (patente,))  # Borrado SQL
            conn.commit()  # Guarda cambios
