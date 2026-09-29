# Importa los modelos del dominio para crear instancias de prueba
from model.cliente import Cliente  # Importa la entidad Cliente
from model.auto import Auto  # Importa la entidad Auto
from model.camion import Camion  # Importa la entidad Camion
from model.moto import Moto  # Importa la entidad Moto

# Importa las clases DAO para simular operaciones de persistencia
from dao.cliente_dao import ClienteDAO  # Importa ClienteDAO


def main():  # Función principal de ejecución del programa
    print("=== SISTEMA TALLER MECÁNICO (DEMO POO + DAO) ===")  # Muestra encabezado en consola

    # 1. INSTANCIACIÓN DE OBJETOS DE DOMINIO (Demostración de POO)
    cliente_demo = Cliente("11111111-1", "Carlos", "Pérez", "+56912345678", "carlos@gmail.com", "Av. Principal 123")  # Instancia un Cliente
    auto_demo = Auto("AB123CD", "Toyota", "Corolla", 2022, num_puertas=4)  # Instancia un Auto
    camion_demo = Camion("XY987ZT", "Volvo", "FH16", 2020, capacidad_ton=18.0)  # Instancia un Camión
    moto_demo = Moto("JK456LM", "Yamaha", "YZF-R3", 2023, cilindrada=321)  # Instancia una Moto

    # 2. DEMOSTRACIÓN DE POLIMORFISMO
    vehiculos = [auto_demo, camion_demo, moto_demo]  # Almacena distintos subtipos en una sola lista
    print("\n--- Demostración de Polimorfismo (Tarifas Diferenciadas) ---")  # Separador visual
    for v in vehiculos:  # Recorre cada vehículo invocando el mismo método .tarifa_hora()
        print(f"Vehículo {v.patente} ({v.__class__.__name__}): ${v.tarifa_hora()}/hora")  # Muestra tarifa específica según el tipo

    # 3. VERIFICACIÓN DE OBJETOS PREPARADOS PARA PERSISTENCIA
    print("\n--- Demostración de Capa POO + DAO ---")  # Separador visual
    print(f"Cliente instanciado en memoria: {cliente_demo.nombre_completo()} (RUT: {cliente_demo.rut})")  # Muestra datos del cliente

    print("\n=== EJECUCIÓN CONCLUIDA CON ÉXITO ===")  # Mensaje final de confirmación


if __name__ == "__main__":  # Bloque estándar de ejecución directa en Python
    main()  # Llama a la función principal
