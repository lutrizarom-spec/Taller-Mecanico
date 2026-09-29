from conectar import obtener_conexion  # Importa la conexión central
from model.rol import Rol  # Importa la clase de dominio Rol
from dao.dao import BaseDAO  # Importa la interfaz BaseDAO


class RolDAO(BaseDAO):  # Implementación DAO para administrar la tabla de Roles

    def crear(self, rol: Rol):  # Inserta un nuevo rol en la base de datos
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("INSERT INTO roles (nombre_rol, descripcion) VALUES (?, ?)", (rol.nombre_rol, rol.descripcion))  # Inserción parametrizada
            conn.commit()  # Guarda cambios

    def obtener_por_id(self, id_rol: int):  # Busca un rol por su ID numérico
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT id_rol, nombre_rol, descripcion FROM roles WHERE id_rol = ?", (id_rol,))  # Filtra por id_rol
            row = cursor.fetchone()  # Obtiene la fila
            return Rol(row["id_rol"], row["nombre_rol"], row["descripcion"]) if row else None  # Convierte a objeto Rol

    def listar_todos(self):  # Obtiene todos los roles del sistema
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("SELECT id_rol, nombre_rol, descripcion FROM roles")  # Consulta
            return [Rol(r["id_rol"], r["nombre_rol"], r["descripcion"]) for r in cursor.fetchall()]  # Mapea a objetos

    def eliminar(self, id_rol: int):  # Elimina un rol por su ID
        with obtener_conexion() as conn:  # Conecta a la BD
            cursor = conn.cursor()  # Obtiene el cursor
            cursor.execute("DELETE FROM roles WHERE id_rol = ?", (id_rol,))  # Borrado SQL
            conn.commit()  # Confirma la acción
