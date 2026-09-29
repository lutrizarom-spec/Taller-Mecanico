from conectar import obtener_conexion  # Importa la conexión central a la BD
from model.vehiculo import Vehiculo  # Importa el modelo Vehiculo
from dao.dao import BaseDAO  # Importa la interfaz DAO base


class VehiculoDAO(BaseDAO):  # Implementación DAO para la entidad Vehiculo

    def crear(self, vehiculo: Vehiculo):  # Inserta un vehículo en la BD
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("INSERT INTO vehiculos (patente, marca, modelo, anio) VALUES (?, ?, ?, ?)",
                           (vehiculo.patente, vehiculo.marca, vehiculo.modelo, vehiculo.anio))  # Ejecuta la inserción
            conn.commit()  # Guarda cambios

    def obtener_por_id(self, patente: str):  # Busca vehículo por patente
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT patente, marca, modelo, anio FROM vehiculos WHERE patente = ?", (patente,))  # Consulta por patente
            row = cursor.fetchone()  # Recupera fila
            return Vehiculo(row["patente"], row["marca"], row["modelo"], row["anio"]) if row else None  # Retorna objeto o None

    def listar_todos(self):  # Lista todos los vehículos
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT patente, marca, modelo, anio FROM vehiculos")  # Consulta general
            return [Vehiculo(r["patente"], r["marca"], r["modelo"], r["anio"]) for r in cursor.fetchall()]  # Retorna lista de vehículos

    def eliminar(self, patente: str):  # Elimina vehículo por patente
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("DELETE FROM vehiculos WHERE patente = ?", (patente,))  # Elimina registro
            conn.commit()  # Guarda cambios
