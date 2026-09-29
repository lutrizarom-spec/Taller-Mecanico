from conectar import obtener_conexion  # Importa la función de conexión a BD
from model.moto import Moto  # Importa la entidad Moto
from dao.dao import BaseDAO  # Importa la interfaz BaseDAO


class MotoDAO(BaseDAO):  # Implementación DAO para la entidad Moto

    def crear(self, moto: Moto):  # Guarda una nueva motocicleta con su cilindrada cc
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute(  # Inserción con atributo cilindrada
                "INSERT INTO motos (patente, marca, modelo, anio, cilindrada, en_taller) VALUES (?, ?, ?, ?, ?, ?)",
                (moto.patente, moto.marca, moto.modelo, moto.anio, moto.cilindrada, int(moto.en_taller))
            )
            conn.commit()  # Confirma la transacción en BD

    def obtener_por_id(self, patente: str):  # Busca una moto por su patente
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT patente, marca, modelo, anio, cilindrada, en_taller FROM motos WHERE patente = ?", (patente,))  # Consulta filtrada
            row = cursor.fetchone()  # Recupera fila
            return Moto(row["patente"], row["marca"], row["modelo"], row["anio"], row["cilindrada"], bool(row["en_taller"])) if row else None  # Instancia Moto

    def listar_todos(self):  # Obtiene todas las motocicletas registradas
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT patente, marca, modelo, anio, cilindrada, en_taller FROM motos")  # Consulta masiva
            return [Moto(r["patente"], r["marca"], r["modelo"], r["anio"], r["cilindrada"], bool(r["en_taller"])) for r in cursor.fetchall()]  # Mapea a lista

    def eliminar(self, patente: str):  # Elimina una moto por su patente
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("DELETE FROM motos WHERE patente = ?", (patente,))  # Ejecuta la eliminación
            conn.commit()  # Guarda cambios
