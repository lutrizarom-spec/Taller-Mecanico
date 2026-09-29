from conectar import obtener_conexion  # Importa la función encargada de abrir la conexión con SQLite


def inicializar_bd():  # Función encargada de crear todas las tablas necesarias si no existen

    # Sentencias DDL para la creación del esquema relacional
    sql_script = """
    -- 1. Tabla de Roles para control de acceso
    CREATE TABLE IF NOT EXISTS roles (
        id_rol INTEGER PRIMARY KEY AUTOINCREMENT,  -- Clave primaria autoincremental
        nombre_rol TEXT NOT NULL,                   -- Nombre del rol (ej: Admin, Mecánico)
        descripcion TEXT                            -- Descripción de los permisos asignados
    );

    -- 2. Tabla de Usuarios vinculada a Roles
    CREATE TABLE IF NOT EXISTS usuarios (
        rut TEXT PRIMARY KEY,                       -- RUT como clave primaria
        nombre TEXT NOT NULL,                       -- Nombre del usuario
        apellido TEXT NOT NULL,                     -- Apellido del usuario
        telefono TEXT,                              -- Teléfono de contacto
        email TEXT,                                 -- Correo electrónico
        username TEXT UNIQUE NOT NULL,              -- Nombre de usuario único para acceso
        clave TEXT NOT NULL,                        -- Contraseña del usuario
        id_rol INTEGER,                             -- Clave foránea referenciando a roles
        FOREIGN KEY (id_rol) REFERENCES roles(id_rol)
    );

    -- 3. Tabla de Clientes
    CREATE TABLE IF NOT EXISTS clientes (
        rut TEXT PRIMARY KEY,                       -- RUT único del cliente
        nombre TEXT NOT NULL,                       -- Nombre del cliente
        apellido TEXT NOT NULL,                     -- Apellido del cliente
        telefono TEXT,                              -- Teléfono de contacto
        email TEXT,                                 -- Correo electrónico
        direccion TEXT                              -- Dirección del cliente
    );

    -- 4. Tabla de Marcas de Vehículos
    CREATE TABLE IF NOT EXISTS marcas (
        id_marca INTEGER PRIMARY KEY AUTOINCREMENT, -- Identificador único de la marca
        nombre TEXT NOT NULL                        -- Nombre de la marca (ej: Toyota)
    );

    -- 5. Tabla de Modelos vinculada a Marcas
    CREATE TABLE IF NOT EXISTS modelos (
        id_modelo INTEGER PRIMARY KEY AUTOINCREMENT,-- Identificador único del modelo
        id_marca INTEGER NOT NULL,                  -- Clave foránea que asocia la marca
        nombre TEXT NOT NULL,                       -- Nombre del modelo (ej: Corolla)
        FOREIGN KEY (id_marca) REFERENCES marcas(id_marca)
    );

    -- 6. Tabla Base de Vehículos Genéricos
    CREATE TABLE IF NOT EXISTS vehiculos (
        patente TEXT PRIMARY KEY,                   -- Patente como clave primaria
        marca TEXT NOT NULL,                        -- Nombre o referencia de marca
        modelo TEXT NOT NULL,                       -- Nombre o referencia de modelo
        anio INTEGER NOT NULL,                      -- Año del vehículo
        en_taller INTEGER DEFAULT 1                 -- Estado: 1 en taller, 0 entregado
    );

    -- 7. Tabla Especializada de Autos
    CREATE TABLE IF NOT EXISTS autos (
        patente TEXT PRIMARY KEY,                   -- Patente del automóvil
        marca TEXT NOT NULL,                        -- Marca del automóvil
        modelo TEXT NOT NULL,                       -- Modelo del automóvil
        anio INTEGER NOT NULL,                      -- Año de fabricación
        num_puertas INTEGER DEFAULT 4,              -- Número de puertas (específico de autos)
        en_taller INTEGER DEFAULT 1                 -- Estado en taller
    );

    -- 8. Tabla Especializada de Camiones
    CREATE TABLE IF NOT EXISTS camiones (
        patente TEXT PRIMARY KEY,                   -- Patente del camión
        marca TEXT NOT NULL,                        -- Marca del camión
        modelo TEXT NOT NULL,                       -- Modelo del camión
        anio INTEGER NOT NULL,                      -- Año de fabricación
        capacidad_ton REAL DEFAULT 5.0,             -- Capacidad en toneladas (específico de camiones)
        en_taller INTEGER DEFAULT 1                 -- Estado en taller
    );

    -- 9. Tabla Especializada de Motocicletas
    CREATE TABLE IF NOT EXISTS motos (
        patente TEXT PRIMARY KEY,                   -- Patente de la moto
        marca TEXT NOT NULL,                        -- Marca de la motocicleta
        modelo TEXT NOT NULL,                       -- Modelo de la motocicleta
        anio INTEGER NOT NULL,                      -- Año de fabricación
        cilindrada INTEGER DEFAULT 150,             -- Cilindrada en cc (específico de motos)
        en_taller INTEGER DEFAULT 1                 -- Estado en taller
    );

    -- 10. Tabla de Repuestos en Inventario
    CREATE TABLE IF NOT EXISTS repuestos (
        id_repuesto INTEGER PRIMARY KEY AUTOINCREMENT, -- ID autoincremental del repuesto
        nombre TEXT NOT NULL,                           -- Nombre del repuesto
        precio REAL NOT NULL,                           -- Precio unitario
        stock INTEGER NOT NULL,                         -- Cantidad disponible en inventario
        descripcion TEXT                                -- Descripción del repuesto
    );

    -- 11. Tabla Transaccional de Órdenes de Trabajo
    CREATE TABLE IF NOT EXISTS ordenes_trabajo (
        id_orden INTEGER PRIMARY KEY AUTOINCREMENT, -- Número de orden de trabajo
        rut_cliente TEXT NOT NULL,                  -- FK del cliente que solicita la orden
        patente_vehiculo TEXT NOT NULL,             -- FK del vehículo a reparar
        id_usuario INTEGER NOT NULL,                -- FK del usuario/operador a cargo
        estado TEXT DEFAULT 'Ingresado',            -- Estado del trabajo
        fecha_ingreso TEXT NOT NULL,                -- Fecha y hora de registro
        FOREIGN KEY (rut_cliente) REFERENCES clientes(rut),
        FOREIGN KEY (patente_vehiculo) REFERENCES vehiculos(patente)
    );

    -- 12. Tabla de Detalle de Repuestos consumidos en Órdenes
    CREATE TABLE IF NOT EXISTS linea_detalle (
        id_detalle INTEGER PRIMARY KEY AUTOINCREMENT, -- ID único del ítem
        id_orden INTEGER NOT NULL,                  -- FK de la orden de trabajo
        id_repuesto INTEGER NOT NULL,               -- FK del repuesto utilizado
        cantidad INTEGER NOT NULL,                  -- Cantidad utilizada
        precio_unitario REAL NOT NULL,              -- Precio de cobro al momento de la orden
        FOREIGN KEY (id_orden) REFERENCES ordenes_trabajo(id_orden),
        FOREIGN KEY (id_repuesto) REFERENCES repuestos(id_repuesto)
    );
    """

    with obtener_conexion() as conn:  # Abre la conexión con la base de datos
        cursor = conn.cursor()  # Obtiene el cursor SQL
        cursor.executescript(sql_script)  # Ejecuta todo el script DDL de creación
        conn.commit()  # Asegura la persistencia del esquema en el archivo taller.db
    
    print("[BD] Esquema de base de datos 'taller.db' verificado/inicializado correctamente.")
