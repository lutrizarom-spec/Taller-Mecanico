from init_db import inicializar_bd  # Importa el inicializador del esquema de base de datos
from model.cliente import Cliente  # Importa el modelo Cliente
from model.auto import Auto  # Importa el modelo Auto
from model.camion import Camion  # Importa el modelo Camion
from model.moto import Moto  # Importa el modelo Moto
from dao.cliente_dao import ClienteDAO  # Importa ClienteDAO


def main():  # Función principal de ejecución del programa
    # 0. INICIALIZACIÓN AUTOMÁTICA DE TABLAS
    inicializar_bd()  # Crea las tablas físicamente en taller.db si aún no existen

    print("\n=== SISTEMA TALLER MECÁNICO (DEMO POO + DAO) ===")  # Encabezado principal

    # 1. INSTANCIACIÓN DE OBJETOS DE DOMINIO (Demostración de POO)
    cliente_demo = Cliente("11111111-1", "Carlos", "Pérez", "+56912345678", "carlos@gmail.com", "Av. Principal 123")  # Instancia Cliente
    auto_demo = Auto("AB123CD", "Toyota", "Corolla", 2022, num_puertas=4)  # Instancia Auto
    camion_demo = Camion("XY987ZT", "Volvo", "FH16", 2020, capacidad_ton=18.0)  # Instancia Camión
    moto_demo = Moto("JK456LM", "Yamaha", "YZF-R3", 2023, cilindrada=321)  # Instancia Moto

    # 2. DEMOSTRACIÓN DE POLIMORFISMO
    vehiculos = [auto_demo, camion_demo, moto_demo]  # Lista heterogénea de vehículos
    print("\n--- Demostración de Polimorfismo (Tarifas Diferenciadas) ---")
    for v in vehiculos:  # Invoca el mismo método .tarifa_hora() en diferentes objetos
        print(f"Vehículo {v.patente} ({v.__class__.__name__}): ${v.tarifa_hora()}/hora")

    # 3. PRUEBA REAL DE PERSISTENCIA DAO EN BASE DE DATOS
    print("\n--- Demostración de Persistencia con DAO ---")
    cliente_dao = ClienteDAO()  # Instancia la clase de acceso a datos de clientes
    
    # Intenta insertar el cliente de prueba en la BD (si ya existe, captura la excepción)
    try:
        cliente_dao.crear(cliente_demo)  # Guarda el objeto cliente_demo en SQLite
        print(f"Cliente '{cliente_demo.nombre_completo()}' guardado exitosamente en la base de datos.")
    except Exception as e:
        print(f"Nota de Persistencia: {e}")

    # Consulta y muestra todos los clientes desde la base de datos física
    clientes_en_bd = cliente_dao.listar_todos()  # Lee los registros de la tabla 'clientes'
    print(f"Total de clientes registrados en 'taller.db': {len(clientes_en_bd)}")

    print("\n=== EJECUCIÓN CONCLUIDA CON ÉXITO ===")  # Mensaje de término


if __name__ == "__main__":  # Punto de entrada estándar
    main()  # Ejecuta la función principal
