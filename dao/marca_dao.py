from dao.dao import Dao
from model.marca import Marca

# ==============================================================================
# PATRÓN DE DISEÑO: DATA ACCESS OBJECT (DAO) & HERENCIA
# ==============================================================================
# Patrón DAO: Desacopla la lógica de negocio de la persistencia de datos.
# El resto del sistema interactúa con objetos 'Marca' y le delega a 'MarcaDao'
# la ejecución de sentencias SQL (INSERT, SELECT, CREATE TABLE, etc.).
#
# Herencia: MarcaDao hereda de la clase base 'Dao', reutilizando la conexión a SQLite
# y el cursor sin tener que reabrir conexiones manualmente en cada método.
# ==============================================================================

class MarcaDao(Dao):
    """
    Data Access Object para la entidad Marca.
    Hereda de la clase base Dao para utilizar la conexión y el cursor.
    """

    def crear_tabla(self) -> None:
        """
        Crea la tabla 'marcas' en la base de datos si no existe.
        Estructura:
        - id: INTEGER PRIMARY KEY AUTOINCREMENT
        - nombre: TEXT NOT NULL
        """
        sql = """
        CREATE TABLE IF NOT EXISTS marcas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
        """
        self.cursor.execute(sql)
        self.conexion.commit()

    def insertar(self, marca: Marca) -> None:
        """
        Inserta un nuevo objeto Marca en la base de datos y le asigna
        su ID auto-generado.

        :param marca: Instancia del modelo Marca a persistir.
        """
        sql = "INSERT INTO marcas (nombre) VALUES (?)"
        self.cursor.execute(sql, (marca.nombre,))
        self.conexion.commit()

        # Recupera la última llave primaria auto-incremental generada por SQLite
        marca.id = self.cursor.lastrowid

    def get_all(self) -> list[Marca]:
        """
        Obtiene todas las marcas registradas en la base de datos.

        :return: Lista de objetos Marca hidratados con datos de la BD.
        """
        sql = "SELECT id, nombre FROM marcas"
        self.cursor.execute(sql)
        filas = self.cursor.fetchall()
        
        marcas = []
        for fila in filas:
            marca = Marca(id=fila[0], nombre=fila[1])
            marcas.append(marca)
        return marcas

    def get_by_id(self, id: int) -> Marca | None:
        """
        Busca una marca por su identificador único (ID).

        :param id: Identificador único de la marca.
        :return: Objeto Marca si existe, o None si no se encuentra.
        """
        sql = "SELECT id, nombre FROM marcas WHERE id = ?"
        self.cursor.execute(sql, (id,))
        fila = self.cursor.fetchone()
        
        if fila is not None:
            return Marca(id=fila[0], nombre=fila[1])
        return None
