from conectar import obtener_conexion  # Importa el gestor de conexión
from model.usuario import Usuario  # Importa el modelo Usuario
from dao.dao import BaseDAO  # Importa la interfaz BaseDAO


class UsuarioDAO(BaseDAO):  # Implementación DAO concreta para Usuarios del sistema

    def crear(self, usuario: Usuario):  # Registra un nuevo usuario en la BD
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute(  # Ejecuta inserción SQL
                "INSERT INTO usuarios (rut, nombre, apellido, telefono, email, username, clave, id_rol) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (usuario.rut, usuario.nombre, usuario.apellido, usuario.telefono, usuario.email, usuario.username, usuario.clave, usuario.id_rol)
            )
            conn.commit()  # Guarda los datos

    def obtener_por_id(self, username: str):  # Busca un usuario por su nombre de cuenta
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT rut, nombre, apellido, telefono, email, username, clave, id_rol FROM usuarios WHERE username = ?", (username,))  # Filtra por username
            row = cursor.fetchone()  # Recupera el resultado
            return Usuario(row["rut"], row["nombre"], row["apellido"], row["telefono"], row["email"], row["username"], row["clave"], row["id_rol"]) if row else None  # Instancia objeto

    def listar_todos(self):  # Obtiene la lista completa de usuarios
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT rut, nombre, apellido, telefono, email, username, clave, id_rol FROM usuarios")  # Consulta SQL
            return [Usuario(r["rut"], r["nombre"], r["apellido"], r["telefono"], r["email"], r["username"], r["clave"], r["id_rol"]) for r in cursor.fetchall()]  # Retorna lista de objetos

    def eliminar(self, username: str):  # Elimina un usuario por su username
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("DELETE FROM usuarios WHERE username = ?", (username,))  # Borra el registro
            conn.commit()  # Guarda cambios
