# Taller Mecánico 🚗🔧

Sistema modular de gestión de taller mecánico desarrollado con principios de Programación Orientada a Objetos (POO), arquitectura limpia, tipado estricto y suite de pruebas unitarias.

**Asignatura:** Programación Orientada a Objetos Seguro  
**Institución:** Inacap  
**Profesor:** Michael Arjel  

---

## 📁 Estructura del Proyecto

```
taller_mecanico/
├── src/
│   ├── __init__.py
│   ├── vehiculo.py        # Clase base Vehiculo con encapsulación y estados
│   ├── auto.py            # Subclase Auto (tarifa $25.000)
│   ├── moto.py            # Subclase Moto (tarifa $15.000)
│   ├── camion.py          # Subclase Camion con TipoCamion y tarifas dinámicas
│   ├── repuesto.py        # Clase Repuesto con control de stock finito
│   ├── usuario.py         # Clase Usuario con saldo deudor y control de retiros
│   └── excepciones.py     # Excepciones de dominio (StockInsuficienteError, DeudaPendienteError)
├── tests/
│   ├── __init__.py
│   ├── test_vehiculo.py   # Pruebas unitarias de Vehículo y subclases (13 tests)
│   ├── test_repuesto.py   # Pruebas unitarias de Repuesto e inventario (6 tests)
│   └── test_usuario.py    # Pruebas unitarias de Usuario y deudas (6 tests)
├── docs/
│   ├── README.md
│   └── DESIGN.md          # Especificación de diseño y arquitectura
├── .gitignore             # Configuración de exclusiones Git
├── main.py                # Simulación integral del flujo de taller con try-except
└── README.md              # Documentación del repositorio
```

---

## 🚀 Ejecución

### Ejecutar Simulación Principal
```bash
python main.py
```

### Ejecutar Pruebas Unitarias
```bash
python -m unittest discover tests
```

---

## 📋 Bitácora de Avances

### 25 de Agosto de 2026
- **Configuración Inicial:** Creación de clase `Vehiculo` y script inicial `main.py`.

### 31 de Agosto de 2026
- **Reestructuración Modular:** Migración a arquitectura empresarial con carpetas `src/`, `tests/` y `docs/`.
- **Encapsulación Robusta:** Incorporación de `@property` getters para acceso seguro a atributos privados.
- **Suite de Pruebas:** Implementación de `tests/test_vehiculo.py` con casos de prueba automatizados.
- **Documentación de Arquitectura:** Creación de `docs/DESIGN.md` detallando el modelo de dominio.

### 7 de Septiembre de 2026
- **Polimorfismo Especializado:** Incorporación de `Auto`, `Moto` y `Camion` con enum `TipoCamion` y recargos por criticidad.
- **Validación de Patente:** Validación chilena estricta (`AA0000` y `AAAA00`).

### 8 de Septiembre de 2026
- **Manejo de Excepciones y Reglas de Negocio:**
  - Creación de `StockInsuficienteError` y módulo `Repuesto` para recursos que se agotan.
  - Creación de `DeudaPendienteError` y módulo `Usuario` con restricción de retiro de vehículos impagos.
  - Ampliación de la suite a 25 pruebas unitarias automatizadas (100% aprobadas).
  - Integración de demostraciones con bloques `try ... except` en `main.py`.
