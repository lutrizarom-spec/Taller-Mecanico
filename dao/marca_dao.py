from dao.dao import Dao  # Importa la clase base Dao desde el módulo dao.dao
from model.marca import Marca  # Importa la clase Marca desde el módulo model.marca

class MarcaDao(Dao):  # Define la clase MarcaDao que hereda de Dao
    """
    Data Access Object para la entidad Marca.
    Hereda de la clase base Dao para utilizar la conexión y el cursor.
    """
    
    def crear_tabla(self):  # Define el método para crear la tabla correspondiente
        """
        Crea la tabla 'marcas' en la base de datos si no existe.
        La tabla contiene:
        - id: INTEGER PRIMARY KEY AUTOINCREMENT
        - nombre: TEXT NOT NULL
        """
        sql = """
        CREATE TABLE IF NOT EXISTS marcas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
        """
        self.cursor.execute(sql)  # Ejecuta la consulta SQL utilizando el cursor heredado
        self.conexion.commit()  # Confirma (guarda) los cambios en la base de datos utilizando la conexión heredada

    def get_all(self):  # Define el método para obtener todas las marcas
        """
        Obtiene todas las marcas registradas en la base de datos.
        
        Returns:
            list[Marca]: Lista de objetos Marca con sus respectivos datos.
        """
        sql = "SELECT id, nombre FROM marcas"  # Sentencia SQL para consultar todos los registros de marcas
        self.cursor.execute(sql)  # Ejecuta la consulta a través del cursor heredado
        filas = self.cursor.fetchall()  # Recupera todas las filas resultantes de la consulta
        marcas = []  # Inicializa una lista vacía para almacenar los objetos Marca
        for fila in filas:  # Itera sobre cada registro (fila) obtenido
            marca = Marca(nombre=fila[1], id=fila[0])  # Instancia un objeto Marca con nombre e id
            marcas.append(marca)  # Agrega la instancia a la lista de marcas
        return marcas  # Retorna la lista con todos los objetos Marca

    def get_all_marcas(self):  # Método alternativo / alias explícito para obtener todas las marcas
        """
        Alias del método get_all para obtener todas las marcas.
        """
        return self.get_all()  # Invoca y retorna el resultado de get_all()

    def get_by_id(self, id_marca: int):  # Define el método para obtener una marca según su ID
        """
        Busca y obtiene una marca por su ID.
        
        Args:
            id_marca (int): El identificador único de la marca en la base de datos.
            
        Returns:
            Marca | None: Objeto Marca si se encuentra, o None si no existe.
        """
        sql = "SELECT id, nombre FROM marcas WHERE id = ?"  # Sentencia SQL parametrizada para buscar por id
        self.cursor.execute(sql, (id_marca,))  # Ejecuta la consulta pasando el id de manera segura
        fila = self.cursor.fetchone()  # Recupera el primer registro que coincida con el criterio
        if fila:  # Verifica si se encontró una fila coincidente
            return Marca(nombre=fila[1], id=fila[0])  # Retorna el objeto Marca con los datos recuperados
        return None  # Retorna None si no se encontró ningún registro

    def get_marca_by_id(self, id_marca: int):  # Método alternativo / alias explícito para buscar marca por ID
        """
        Alias del método get_by_id para obtener una marca por su ID.
        """
        return self.get_by_id(id_marca)  # Invoca y retorna el resultado de get_by_id()

    def obtener_todas(self):  # Alias en español para obtener todas las marcas
        """
        Alias en español que invoca a get_all.
        """
        return self.get_all()  # Invoca y retorna el resultado de get_all()

    def obtener_por_id(self, id_marca: int):  # Alias en español para obtener una marca por su ID
        """
        Alias en español que invoca a get_by_id.
        """
        return self.get_by_id(id_marca)  # Invoca y retorna el resultado de get_by_id()
