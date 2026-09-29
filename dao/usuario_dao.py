from conectar import obtener_conexion  # Importa la conexión central a la BD
from model.usuario import Usuario  # Importa el modelo Usuario
from dao.dao import BaseDAO  # Importa la interfaz DAO base


class UsuarioDAO(BaseDAO):  # Implementación DAO para la entidad Usuario

    def crear(self, usuario: Usuario):  # Registra un nuevo usuario
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute(  # Inserta los datos del usuario
                "INSERT INTO usuarios (rut, nombre, apellido, telefono, email, username, clave, rol) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (usuario.rut, usuario.nombre, usuario.apellido, usuario.telefono, usuario.email, usuario.username, usuario.clave, usuario.rol)
            )
            conn.commit()  # Guarda los cambios

    def obtener_por_id(self, username: str):  # Busca un usuario por su nombre de usuario
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT rut, nombre, apellido, telefono, email, username, clave, rol FROM usuarios WHERE username = ?", (username,))  # Consulta filtrada
            row = cursor.fetchone()  # Recupera la coincidencia
            return Usuario(row["rut"], row["nombre"], row["apellido"], row["telefono"], row["email"], row["username"], row["clave"], row["rol"]) if row else None  # Convierte a objeto

    def listar_todos(self):  # Obtiene la lista completa de usuarios
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT rut, nombre, apellido, telefono, email, username, clave, rol FROM usuarios")  # Consulta general
            return [Usuario(r["rut"], r["nombre"], r["apellido"], r["telefono"], r["email"], r["username"], r["clave"], r["rol"]) for r in cursor.fetchall()]  # Retorna lista

    def eliminar(self, username: str):  # Elimina un usuario por username
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("DELETE FROM usuarios WHERE username = ?", (username,))  # Elimina la fila
            conn.commit()  # Guarda los cambios
