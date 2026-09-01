"""
SISTEMA DE GESTIÓN DE TALLER MECÁNICO
Script Principal (main.py): Simulación de flujo de trabajo con Vehiculo.
"""

import sys  # Importa sys para configuración de codificación de salida
from src.vehiculo import Vehiculo  # Importa la clase Vehiculo desde el paquete modular src

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")  # Garantiza compatibilidad UTF-8 en consola Windows


def ejecutar_simulacion() -> None:  # Función principal que orquesta la simulación
    print("=" * 60)  # Separador visual de encabezado
    print("       🚗 SISTEMA DE GESTIÓN - TALLER MECÁNICO 🔧")  # Título principal
    print("=" * 60)  # Cierre del separador

    # 1. Instanciación del Vehículo
    print("\n[PASO 1] 🚙 Creación y Registro del Vehículo:")  # Encabezado del paso 1
    auto = Vehiculo(patente="ABC123", anio=2020)  # Crea la instancia con patente y año
    print(f"  * {auto}")  # Muestra el estado inicial del objeto
    print(f"  * Tarifa por hora base: ${auto.tarifa_hora():,}")  # Muestra la tarifa configurada

    # 2. Registro de Ingreso al Taller
    print("\n[PASO 2] 📥 Ingreso del Vehículo al Taller:")  # Encabezado del paso 2
    resultado_ingreso = auto.ingresar()  # Intento de ingreso al taller
    print(f"  * Acción: {resultado_ingreso}")  # Muestra el mensaje retornado
    print(f"  * Estado actual: {auto}")  # Muestra el estado actualizado

    # 3. Validación de intento de re-ingreso (Comportamiento defensivo)
    print("\n[PASO 3] ⚠️ Validación de Re-ingreso Duplicado:")  # Encabezado del paso 3
    resultado_reingreso = auto.ingresar()  # Re-intento mientras ya está dentro
    print(f"  * Acción: {resultado_reingreso}")  # Mensaje defensivo

    # 4. Registro de Salida / Entrega del Vehículo
    print("\n[PASO 4] 📤 Salida y Entrega del Vehículo:")  # Encabezado del paso 4
    resultado_entrega = auto.entregar()  # Ejecuta la entrega
    print(f"  * Acción: {resultado_entrega}")  # Muestra el mensaje retornado
    print(f"  * Estado final: {auto}")  # Muestra el estado final

    print("\n" + "=" * 60)  # Separador de pie
    print("           ✅ SIMULACIÓN COMPLETADA CON ÉXITO")  # Mensaje de término
    print("=" * 60)  # Cierre


if __name__ == "__main__":  # Punto de entrada de ejecución del script
    ejecutar_simulacion()  # Llama a la simulación
