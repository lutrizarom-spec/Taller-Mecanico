from conectar import obtener_conexion  # Importa el gestor de conexiones
from model.auto import Auto  # Importa el modelo Auto
from dao.dao import BaseDAO  # Importa la interfaz BaseDAO


class AutoDAO(BaseDAO):  # Implementación DAO específica para Automóviles

    def crear(self, auto: Auto):  # Inserta un auto con su número de puertas
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute(  # Ejecuta inserción con num_puertas
                "INSERT INTO autos (patente, marca, modelo, anio, num_puertas, en_taller) VALUES (?, ?, ?, ?, ?, ?)",
                (auto.patente, auto.marca, auto.modelo, auto.anio, auto.num_puertas, int(auto.en_taller))
            )
            conn.commit()  # Guarda los cambios

    def obtener_por_id(self, patente: str):  # Busca un auto por su patente
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT patente, marca, modelo, anio, num_puertas, en_taller FROM autos WHERE patente = ?", (patente,))  # Consulta filtrada
            row = cursor.fetchone()  # Recupera registro
            return Auto(row["patente"], row["marca"], row["modelo"], row["anio"], row["num_puertas"], bool(row["en_taller"])) if row else None  # Mapea a Auto

    def listar_todos(self):  # Obtiene el listado completo de autos
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT patente, marca, modelo, anio, num_puertas, en_taller FROM autos")  # Consulta general
            return [Auto(r["patente"], r["marca"], r["modelo"], r["anio"], r["num_puertas"], bool(r["en_taller"])) for r in cursor.fetchall()]  # Mapea a lista

    def eliminar(self, patente: str):  # Elimina un auto por su patente
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("DELETE FROM autos WHERE patente = ?", (patente,))  # Borra registro
            conn.commit()  # Guarda cambios
