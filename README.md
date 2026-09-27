# Taller Mecánico

Repositorio para la asignatura de Programación Orientada a Objetos Seguro.

**Profesor:** Michael Arjel
**Institución:** Inacap

---

## Bitácora de Avances

### 25 de Agosto de 2026
- **Configuración Inicial:** Vinculación del directorio local con el repositorio de GitHub usando el CLI de GitHub (`gh auth`).
- **Limpieza:** Se eliminó la versión antigua del archivo `vehiculo.py` para construir el proyecto desde cero.
- **Clase Vehiculo (`vehiculo.py`):**
  - Se creó la clase principal del proyecto.
  - Se definieron los atributos privados `__patente`, `__anio` y `__en_taller` en el constructor, aplicando encapsulamiento y *type hints*.
  - Se crearon los métodos `ingresar()` y `entregar()` con validación de estado.
  - Se creó el método `tarifa_hora()` que retorna un valor fijo de 5000.
- **Script de Pruebas (`main.py`):**
  - Se creó el archivo de ejecución principal.
  - Se importó la clase `Vehiculo` y se instanciaron 3 objetos con datos ficticios.
  - Se probó la invocación de métodos y la impresión de la tarifa por hora en consola.
- **Documentación:** Se comentaron todas las líneas de código en ambos archivos (`vehiculo.py` y `main.py`) explicando paso a paso su funcionamiento con fines educativos.

### 31 de Agosto de 2026
- **Creación de Rama de Trabajo:** Creación y publicación de la rama `feature/desarrollo`.
- **Implementación de Herencia (Subclases):**
  - **Clase Auto (`auto.py`):** Hereda de `Vehiculo`, implementa su propio constructor invocando a `super()` y añade el atributo privado `__capacidad_maletero` (en litros).
  - **Clase Moto (`moto.py`):** Hereda de `Vehiculo` (estructura base).
  - **Clase Camion (`camion.py`):** Hereda de `Vehiculo`, implementa su propio constructor invocando a `super()` y añade el atributo privado `__capacidad_carga` (en kilos).
- **Actualización de Script Principal (`main.py`):**
  - Se importaron las subclases `Auto`, `Moto` y `Camion`.
  - Se instanciaron objetos de cada una de las clases hijas y se verificó la invocación de métodos heredados (`ingresar()` y `tarifa_hora()`).
- **Documentación:** Código comentado línea por línea con fines pedagógicos.

### 15 de Septiembre de 2026
- **Integración con SQLite:**
  - Creación del archivo `conectar.py` con una función `crear_conexion()` que establece la conexión a la base de datos `taller.db` y habilita el uso de Foreign Keys (`PRAGMA foreign_keys = ON`).
- **Refactorización de Arquitectura (MVC/DAO):**
  - Creación de los paquetes (carpetas) `model` y `dao`, añadiendo en ambos el archivo `__init__.py`.
  - Migración de todas las clases del dominio (vehículos, personas, órdenes, etc.) a la carpeta `model` y actualización masiva de los imports en el proyecto.
- **Implementación del Patrón DAO (Data Access Object):**
  - **`dao.py` (Clase Base):** Gestiona la recepción de la conexión y establece el cursor para ser reutilizado.
  - **`marca_dao.py` y `modelo_dao.py`:** Clases hijas que heredan de `Dao` e incluyen el método `crear_tabla()`. Implementan llaves foráneas (FK) relacionando un Modelo a una Marca.
  - **`vehiculo_dao.py` y `auto_dao.py`:** Implementación de herencia relacional (Table-per-type). `AutoDao` hereda de `VehiculoDao` e invoca `super().crear_tabla()`. La tabla `autos` usa su llave primaria también como llave foránea hacia `vehiculos`.
- **Actualización de Script Principal (`main.py`):**
  - El código de prueba fue refactorizado y limpiado para enfocarse únicamente en inicializar los DAOs y crear (o validar la existencia de) las tablas correspondientes (`marcas`, `modelos`, `vehiculos`, `autos`).

### 21 de Septiembre de 2026
- **Implementación de método de Inserción (CRUD):**
  - **`marca_dao.py`:** Se agregó el método `insertar()` para registrar nuevas marcas en la base de datos y recuperar el ID generado automáticamente mediante `lastrowid`.
  - **`marca.py`:** Se actualizó el modelo para incluir el atributo `id` con sus respectivos métodos *getter* y *setter*.
- **Actualización de Script Principal (`main.py`):**
  - Se adaptó el código para probar específicamente la inserción de una `Marca`, demostrando cómo el `id` pasa de `None` a un número válido tras guardar en la base de datos.
  - El código de creación de tablas original fue comentado para que sirva de referencia de estudio a los alumnos.

### 22 de Septiembre de 2026
- **Documentación Exhaustiva:** Se agregó un comentario explicativo en línea a absolutamente todas las sentencias y declaraciones de código en los paquetes `model` y `dao`, con el fin de facilitar el estudio y comprensión del funcionamiento interno por parte de los alumnos.
- **Gestión de Ramas (Homologación):** Se fusionaron y homologaron los cambios de la rama de desarrollo hacia la rama principal (`master`).
- **Publicación:** Publicación de la versión finalizada usando la cuenta autorizada (`michaelarjelm`).
