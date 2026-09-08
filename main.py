"""
SISTEMA DE GESTIÓN DE TALLER MECÁNICO
Script Principal (main.py): Validación de Encapsulamiento (@property) y Polimorfismo.
"""

import sys  # Importa sys para configuración de codificación de salida
from src.vehiculo import Vehiculo  # Importa la clase Vehiculo base
from src.auto import Auto  # Importa la clase Auto
from src.moto import Moto  # Importa la clase Moto
from src.camion import Camion, TipoCamion  # Importa la clase Camion y el enum TipoCamion
from src.repuesto import Repuesto  # Importa la clase Repuesto para control de inventario
from src.usuario import Usuario  # Importa la clase Usuario para control de clientes y deudas
from src.excepciones import StockInsuficienteError, DeudaPendienteError  # Excepciones de negocio

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")  # Garantiza compatibilidad UTF-8 en consola Windows


def ejecutar_simulacion() -> None:  # Función principal que orquesta la simulación
    print("=" * 65)
    print("   🚗 VALIDACIÓN DE ENCAPSULAMIENTO Y POLIMORFISMO 🔧")
    print("=" * 65)

    # 1. Prueba de Polimorfismo en Tarifas
    print("\n[PASO 1] 🔄 Lista Polimórfica y Tarifas:")
    vehiculos = [
        Auto(patente="AUTO12", anio=2021),
        Moto(patente="MOTO34", anio=2022),
        Camion(patente="CAMI56", anio=2019, capacidad_carga=5000)
    ]
    for v in vehiculos:
        print(f"  * {type(v).__name__} ({v.patente}) -> Tarifa: ${v.tarifa_hora():,}")

    # 2. Prueba de Clase Abstracta (Vehiculo no instanciable directamente)
    print("\n[PASO 2A] 🏛️ Demostración de Clase Abstracta ABC (espera TypeError):")
    try:
        Vehiculo(patente="AB1234", anio=2020)  # Intento de instanciación directa de clase abstracta
    except TypeError as e:
        print(f"  * ✅ Capturado TypeError con éxito: {e}")

    # 2B. Prueba de Validación de Setter (@property patente)
    print("\n[PASO 2B] 🛡️ Validación de Patente Inválida (espera ValueError):")
    try:
        Auto(patente="AB 12", anio=2020)  # Con espacio y menos de 6 caracteres
    except ValueError as e:
        print(f"  * ✅ Capturado ValueError con éxito: {e}")

    # 3. Prueba de Inmutabilidad de Estado (@property en_taller de solo lectura)
    print("\n[PASO 3] 🔒 Bloqueo de Escritura Directa en 'en_taller' (espera AttributeError):")
    auto_prueba = Auto(patente="PRUE01", anio=2023)
    try:
        auto_prueba.en_taller = True  # Intento de modificación directa sin usar ingresar()
    except AttributeError as e:
        print(f"  * ✅ Capturado AttributeError con éxito: {e}")

    # 4. Demostración de Tipos de Camión y Recargos
    print("\n[PASO 4] 🚛 Tipos de Camión y Recargos Tarifarios:")
    camiones = [
        Camion(patente="RAMP01", anio=2021, capacidad_carga=8000, tipo=TipoCamion.RAMPLA_NORMAL),
        Camion(patente="DOBL02", anio=2022, capacidad_carga=12000, tipo=TipoCamion.DOBLE_RAMPLA),
        Camion(patente="EXPL03", anio=2023, capacidad_carga=5000, tipo=TipoCamion.TRANSPORTE_EXPLOSIVOS),
    ]
    for c in camiones:
        print(f"  * {c.tipo.value} ({c.patente}, {c.capacidad_carga} kg) -> Tarifa: ${c.tarifa_hora():,}")

    # 5. Prueba de Regla de Negocio: Stock de Repuesto que se Agota (try-except StockInsuficienteError)
    print("\n[PASO 5] 📦 Control de Stock en Repuestos (espera StockInsuficienteError):")
    filtro = Repuesto(codigo="FILT-01", nombre="Filtro de Aceite Sintético", precio=12000, stock=3)
    print(f"  * Estado inicial: {filtro}")
    print("  * Usando 2 unidades para un servicio...")
    filtro.usar(2)
    print(f"  * Stock restante: {filtro.stock} u.")
    print("  * Intentando usar 3 unidades más (supera las disponibles)...")
    try:
        filtro.usar(3)
    except StockInsuficienteError as e:
        print(f"  * ✅ Capturada excepción de negocio: {e}")
        print(f"    [Detalle] Solicitado: {e.solicitado} u. | Disponible: {e.disponible} u.")

    # 6. Prueba de Regla de Negocio: Usuario con Deuda que Intenta Retirar Vehículo (try-except DeudaPendienteError)
    print("\n[PASO 6] 👤 Control de Retiro de Vehículo según Deuda de Usuario (espera DeudaPendienteError):")
    cliente = Usuario(rut="15432987-K", nombre="Marcela Contreras", deuda=35000)
    auto_cliente = Auto(patente="MARC22", anio=2022)
    auto_cliente.ingresar()
    print(f"  * {cliente}")
    print(f"  * Estado del vehículo: {auto_cliente}")
    print("  * Intentando retirar vehículo con deuda pendiente...")
    try:
        cliente.retirar_vehiculo(auto_cliente)
    except DeudaPendienteError as e:
        print(f"  * ✅ Retiro bloqueado con éxito: {e}")
        print(f"    [Detalle] Deuda activa: ${e.deuda:,}")

    print("  * Cliente abona $35.000 y liquida su deuda...")
    cliente.pagar_deuda(35000)
    print(f"  * Nuevo estado: {cliente}")
    resultado_entrega = cliente.retirar_vehiculo(auto_cliente)
    print(f"  * ✅ Reintento de retiro: {resultado_entrega} ({auto_cliente})")

    print("\n" + "=" * 65)
    print("           ✅ SIMULACIÓN Y VALIDACIONES COMPLETADAS")
    print("=" * 65)


if __name__ == "__main__":
    ejecutar_simulacion()
