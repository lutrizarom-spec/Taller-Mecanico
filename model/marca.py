# ==============================================================================
# PILAR POO: ENCAPSULAMIENTO & ABSTRACCIÓN
# ==============================================================================
# Abstracción: Se modela la entidad 'Marca' del mundo real extrayendo solo sus
# características esenciales (id y nombre) relevantes para el taller mecánico.
#
# Encapsulamiento: Los atributos se declaran privados mediante el prefijo '__'
# (Name Mangling en Python), impidiendo acceso o modificación directa no controlada
# desde el exterior. El acceso y modificación se regula mediante decoradores @property
# (Getters) y @<atributo>.setter (Setters).
# ==============================================================================

class Marca:
    """
    Representa una marca de vehículos en el sistema (ej: Toyota, Ford, Chevrolet).
    """

    def __init__(self, nombre: str, id: int = None):
        """
        Constructor de la clase Marca.
        :param nombre: Cadena con el nombre de la marca.
        :param id: Entero opcional con el ID único asignado por la base de datos (None antes de persistir).
        """
        self.__id = id          # Atributo privado: Identificador único en BD
        self.__nombre = nombre  # Atributo privado: Nombre descriptivo de la marca

    # --------------------------------------------------------------------------
    # GETTERS Y SETTERS (Control de Acceso Encapsulado)
    # --------------------------------------------------------------------------

    @property
    def id(self) -> int:
        """Getter: Permite consultar el ID de la marca sin exponer el atributo privado directamente."""
        return self.__id

    @id.setter
    def id(self, valor: int) -> None:
        """Setter: Permite asignar o actualizar el ID una vez generado por la BD."""
        if valor is not None and valor <= 0:
            raise ValueError("El ID de la marca debe ser un número entero positivo.")
        self.__id = valor

    @property
    def nombre(self) -> str:
        """Getter: Permite consultar el nombre de la marca."""
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        """Setter: Permite modificar el nombre aplicando validación de datos."""
        if not valor or not valor.strip():
            raise ValueError("El nombre de la marca no puede estar vacío.")
        self.__nombre = valor.strip()

    # --------------------------------------------------------------------------
    # POLIMORFISMO: SOBRESCRITURA DE MÉTODOS MÁGICOS DE OBJECT
    # --------------------------------------------------------------------------

    def __repr__(self) -> str:
        """Representación técnica del objeto (ideal para debugging y logs)."""
        return f"Marca(id={self.__id}, nombre='{self.__nombre}')"

    def __str__(self) -> str:
        """Representación legible para el usuario final."""
        return f"Marca #{self.__id or 'Sin ID'}: {self.__nombre}"
