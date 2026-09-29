from conectar import obtener_conexion  # Importa la función de conexión a la BD
from model.cliente import Cliente  # Importa el modelo Cliente
from dao.dao import BaseDAO  # Importa la interfaz abstracta base


class ClienteDAO(BaseDAO):  # Implementación DAO concreta para la entidad Cliente

    def crear(self, cliente: Cliente):  # Inserta un objeto Cliente en la BD
        with obtener_conexion() as conn:  # Contexto de conexión segura
            cursor = conn.cursor()  # Obtiene el cursor SQL
            cursor.execute(  # Ejecuta inserción con parámetros
                "INSERT INTO clientes (rut, nombre, apellido, telefono, email, direccion) VALUES (?, ?, ?, ?, ?, ?)",
                (cliente.rut, cliente.nombre, cliente.apellido, cliente.telefono, cliente.email, cliente.direccion)
            )
            conn.commit()  # Guarda los cambios permanentemente en la BD

    def obtener_por_id(self, rut: str):  # Busca un cliente por su clave primaria (RUT)
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT rut, nombre, apellido, telefono, email, direccion FROM clientes WHERE rut = ?", (rut,))  # Consulta filtrada
            row = cursor.fetchone()  # Recupera el primer registro devuelto
            return Cliente(row["rut"], row["nombre"], row["apellido"], row["telefono"], row["email"], row["direccion"]) if row else None  # Mapea a objeto Cliente

    def listar_todos(self):  # Obtiene la lista completa de clientes registrados
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT rut, nombre, apellido, telefono, email, direccion FROM clientes")  # Consulta masiva
            return [Cliente(r["rut"], r["nombre"], r["apellido"], r["telefono"], r["email"], r["direccion"]) for r in cursor.fetchall()]  # Mapea filas a lista de objetos

    def eliminar(self, rut: str):  # Borra un cliente según su RUT
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("DELETE FROM clientes WHERE rut = ?", (rut,))  # Elimina la fila de la tabla
            conn.commit()  # Confirma el borrado
