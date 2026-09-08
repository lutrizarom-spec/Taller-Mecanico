# 📐 Documento de Diseño y Arquitectura — Taller Mecánico

## 1. Visión General del Sistema
El sistema **Taller Mecánico** es una solución de gestión modular y orientada a objetos (POO) diseñada bajo estándares de ingeniería de software limpios y principios SOLID. Su objetivo principal es modelar de forma precisa el ciclo de vida del vehículo, los servicios de mantenimiento, la asignación de mecánicos y la facturación.

---

## 2. Arquitectura de Paquetes
```
taller_mecanico/
├── src/
│   ├── __init__.py
│   └── vehiculo.py        # Entidad Vehículo con encapsulamiento estricto
├── tests/
│   ├── __init__.py
│   └── test_vehiculo.py   # Suite de pruebas unitarias
├── docs/
│   ├── README.md
│   └── DESIGN.md          # Especificación arquitectónica y de diseño
├── main.py                # Punto de entrada y simulación paso a paso
└── README.md              # Documentación de alto nivel del repositorio
```

---

## 3. Modelo de Dominio

### 3.1 Clase Abstracta `Vehiculo(ABC)`
- **Contrato Abstracto:** Hereda de `abc.ABC`. No permite instanciación directa (`TypeError`).
- **Atributos Privados:**
  - `__patente: str`: Identificador único de placa patente.
  - `__anio: int`: Año de fabricación del modelo.
  - `__en_taller: bool`: Estado binario de permanencia en las instalaciones.
- **Métodos Principales:**
  - `ingresar() -> str`: Controla la transición de estado a "En Taller", con validación de no re-ingreso.
  - `entregar() -> str`: Controla la transición de estado a "Fuera de Taller", validando que esté previamente ingresado.
  - `@abstractmethod tarifa_hora() -> int`: Contrato abstracto obligatorio que cada subclase concreta debe implementar.
- **Properties:**
  - `patente`: Con validación de formato oficial chileno (`AA0000` o `AAAA00`).
  - `anio`, `en_taller`: Con encapsulamiento y control de acceso.

### 3.2 Especialización y Polimorfismo
- **`Auto`:** Tarifa horaria de $25.000.
- **`Moto`:** Tarifa horaria de $15.000.
- **`Camion`:** Incorpora `capacidad_carga` (>0) y `tipo` mediante `TipoCamion` (`RAMPLA_NORMAL`: $40.000, `DOBLE_RAMPLA`: $50.000, `TRANSPORTE_EXPLOSIVOS`: $60.000).

### 3.3 Módulos de Inventario y Actores
- **`Repuesto`:** Control de stock e insumos finitos con validación de cantidad y lanzamiento de `StockInsuficienteError` ante intentos de consumo superiores a la disponibilidad.
- **`Usuario`:** Modelo de cliente/usuario del taller con control de RUT, nombre y saldo deudor (`deuda`). Restringe la entrega de vehículos mediante `DeudaPendienteError` si registra saldos impagos.
- **Excepciones de Dominio (`src/excepciones.py`):**
  - `TallerError`: Clase base.
  - `StockInsuficienteError`: Señaliza quiebre de stock en operaciones de taller.
  - `DeudaPendienteError`: Impide la entrega de vehículos a clientes con deuda.

### 3.4 Extensibilidad Futura (Módulos Siguientes)
- **`Mecanico` (Herencia de `Persona`):** Modelado de personal técnico.
- **`Servicio`:** Catálogo de operaciones técnicas.
- **`OrdenTrabajo` / `Taller`:** Agregación que coordina vehículo, cliente, mecánico y cálculo financiero total.

---

## 4. Estrategia de Calidad y Pruebas
Las pruebas unitarias implementadas en `tests/test_vehiculo.py` cubren:
1. Instanciación y verificación de atributos iniciales.
2. Transición de estado válida en `ingresar()`.
3. Manejo de excepciones / defensas ante re-ingreso duplicado.
4. Transición de estado válida en `entregar()`.
5. Validación defensiva de entrega cuando el vehículo no está en taller.
6. Retorno correcto del cálculo de tarifa horaria.
