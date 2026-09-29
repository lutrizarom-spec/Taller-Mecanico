from abc import ABC, abstractmethod  # Importa componentes para crear clases e interfaces abstractas


class BaseDAO(ABC):  # Clase base abstracta que define el contrato DAO

    @abstractmethod
    def crear(self, objeto):  # Método abstracto para insertar registros
        pass

    @abstractmethod
    def obtener_por_id(self, id_val):  # Método abstracto para buscar por clave primaria
        pass

    @abstractmethod
    def listar_todos(self):  # Método abstracto para listar todos los registros
        pass

    @abstractmethod
    def eliminar(self, id_val):  # Método abstracto para eliminar registros
        pass
