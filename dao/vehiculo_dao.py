from conectar import obtener_conexion  # Importa el gestor de conexiones
from model.vehiculo import Vehiculo  # Importa el modelo base Vehiculo
from dao.dao import BaseDAO  # Importa la interfaz BaseDAO


class VehiculoDAO(BaseDAO):  # Implementación DAO para la tabla base de vehículos

    def crear(self, vehiculo: Vehiculo):  # Inserta un vehículo genérico en la BD
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute(  # Inserta datos del vehículo incluyendo estado en_taller
                "INSERT INTO vehiculos (patente, marca, modelo, anio, en_taller) VALUES (?, ?, ?, ?, ?)",
                (vehiculo.patente, vehiculo.marca, vehiculo.modelo, vehiculo.anio, int(vehiculo.en_taller))
            )
            conn.commit()  # Guarda en la BD

    def obtener_por_id(self, patente: str):  # Busca un vehículo por su patente
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT patente, marca, modelo, anio, en_taller FROM vehiculos WHERE patente = ?", (patente,))  # Búsqueda SQL
            row = cursor.fetchone()  # Recupera fila
            return Vehiculo(row["patente"], row["marca"], row["modelo"], row["anio"], bool(row["en_taller"])) if row else None  # Convierte a objeto

    def listar_todos(self):  # Lista todos los vehículos genéricos
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT patente, marca, modelo, anio, en_taller FROM vehiculos")  # Consulta general
            return [Vehiculo(r["patente"], r["marca"], r["modelo"], r["anio"], bool(r["en_taller"])) for r in cursor.fetchall()]  # Mapea a lista

    def eliminar(self, patente: str):  # Elimina un vehículo por su patente
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("DELETE FROM vehiculos WHERE patente = ?", (patente,))  # Borra registro
            conn.commit()  # Confirma borrado
