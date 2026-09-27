"""
==============================================================================
PUNTO DE ENTRADA Y DEMOSTRACIÓN DE ARQUITECTURA
==============================================================================
Este archivo demuestra la orquestación entre:
1. Conexión SQLite centralizada (`conectar.py`).
2. Capa DAO (Data Access Object): Persistencia y consultas SQLite.
3. Capa Model: Clases del dominio con Encapsulamiento, Abstracción y Polimorfismo.
==============================================================================
"""

from conectar import crear_conexion
from dao.marca_dao import MarcaDao
from dao.modelo_dao import ModeloDao
from dao.vehiculo_dao import VehiculoDao
from dao.auto_dao import AutoDao
from model.marca import Marca


def main():
    print("=" * 65)
    print("  SISTEMA DE GESTIÓN DE TALLER MECÁNICO (DEMO POO + DAO)")
    print("=" * 65)

    # --------------------------------------------------------------------------
    # 0. ESTABLECER CONEXIÓN A BASE DE DATOS
    # --------------------------------------------------------------------------
    conexion = crear_conexion()

    # --------------------------------------------------------------------------
    # 1. INICIALIZACIÓN DE TABLAS (PATRÓN DAO Y HERENCIA)
    # --------------------------------------------------------------------------
    print("\n[1] Inicializando DAOs e inyectando conexión...")
    marca_dao = MarcaDao(conexion)
    modelo_dao = ModeloDao(conexion)
    vehiculo_dao = VehiculoDao(conexion)
    auto_dao = AutoDao(conexion)

    print("    Creando/verificando tablas en SQLite...")
    marca_dao.crear_tabla()
    modelo_dao.crear_tabla()
    vehiculo_dao.crear_tabla()
    auto_dao.crear_tabla()
    print("    ✔ Tablas verificadas / creadas correctamente.")

    # --------------------------------------------------------------------------
    # 2. PRUEBA DE INSERCIÓN Y ENCAPSULAMIENTO
    # --------------------------------------------------------------------------
    print("\n[2] Probando creación de modelo Marca e inserción en BD...")
    nueva_marca = Marca(nombre="Nissan")
    print(f"    -> Estado inicial del objeto (antes de persistir): {nueva_marca} (id={nueva_marca.id})")

    marca_dao.insertar(nueva_marca)
    print(f"    -> Estado tras llamar a marca_dao.insertar():     {nueva_marca} (id={nueva_marca.id})")

    # --------------------------------------------------------------------------
    # 3. PRUEBA DE CONSULTAS (get_all y get_by_id)
    # --------------------------------------------------------------------------
    print("\n[3] Listando todas las marcas registradas (get_all)...")
    todas_las_marcas = marca_dao.get_all()
    for m in todas_las_marcas:
        print(f"    • {m}")

    print("\n[4] Consultando marca por ID (get_by_id)...")
    if nueva_marca.id:
        marca_encontrada = marca_dao.get_by_id(nueva_marca.id)
        print(f"    ✔ Marca recuperada de BD: {marca_encontrada}")

    conexion.close()
    print("\n" + "=" * 65)
    print("  ✔ Demostración completada con éxito. Conexión cerrada.")
    print("=" * 65)


if __name__ == "__main__":
    main()
