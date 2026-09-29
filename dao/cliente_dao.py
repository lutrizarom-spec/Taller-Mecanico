from conectar import obtener_conexion  # Importa la conexión central a la BD
from model.cliente import Cliente  # Importa el modelo Cliente
from dao.dao import BaseDAO  # Importa la interfaz DAO base


class ClienteDAO(BaseDAO):  # Implementación DAO para la entidad Cliente

    def crear(self, cliente: Cliente):  # Guarda un cliente nuevo en SQLite
        with obtener_conexion() as conn:  # Abre la conexión con contexto seguro
            cursor = conn.cursor()  # Obtiene el cursor SQL
            cursor.execute(  # Ejecuta la inserción
                "INSERT INTO clientes (rut, nombre, apellido, telefono, email, direccion) VALUES (?, ?, ?, ?, ?, ?)",
                (cliente.rut, cliente.nombre, cliente.apellido, cliente.telefono, cliente.email, cliente.direccion)
            )
            conn.commit()  # Confirma los cambios en la BD

    def obtener_por_id(self, rut: str):  # Busca un cliente por su RUT
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT rut, nombre, apellido, telefono, email, direccion FROM clientes WHERE rut = ?", (rut,))  # Consulta parametrizada
            row = cursor.fetchone()  # Recupera la primera fila
            return Cliente(row["rut"], row["nombre"], row["apellido"], row["telefono"], row["email"], row["direccion"]) if row else None  # Instancia Cliente o None

    def listar_todos(self):  # Obtiene todos los clientes
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT rut, nombre, apellido, telefono, email, direccion FROM clientes")  # Consulta todos los registros
            return [Cliente(r["rut"], r["nombre"], r["apellido"], r["telefono"], r["email"], r["direccion"]) for r in cursor.fetchall()]  # Retorna lista de objetos

    def eliminar(self, rut: str):  # Elimina un cliente por su RUT
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("DELETE FROM clientes WHERE rut = ?", (rut,))  # Ejecuta el borrado
            conn.commit()  # Guarda el cambio en la BD
