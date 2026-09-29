from abc import ABC, abstractmethod  # Módulo nativo para la definición de Clases Abstractas e Interfaces


class BaseDAO(ABC):  # Clase abstracta que estandariza las operaciones CRUD en la capa DAO

    @abstractmethod
    def crear(self, objeto):  # Método obligatorio para inserción de registros
        pass

    @abstractmethod
    def obtener_por_id(self, id_val):  # Método obligatorio para búsqueda por clave primaria
        pass

    @abstractmethod
    def listar_todos(self):  # Método obligatorio para la lectura masiva de datos
        pass

    @abstractmethod
    def eliminar(self, id_val):  # Método obligatorio para la eliminación de registros
        pass
