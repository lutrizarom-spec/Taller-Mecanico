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

### 3.1 Clase `Vehiculo`
- **Atributos Privados:**
  - `__patente: str`: Identificador único de placa patente.
  - `__anio: int`: Año de fabricación del modelo.
  - `__en_taller: bool`: Estado binario de permanencia en las instalaciones.
- **Métodos Principales:**
  - `ingresar() -> str`: Controla la transición de estado a "En Taller", con validación de no re-ingreso.
  - `entregar() -> str`: Controla la transición de estado a "Fuera de Taller", validando que esté previamente ingresado.
  - `tarifa_hora() -> int`: Retorna la base tarifaria por hora ($5.000).
- **Properties:**
  - `patente`, `anio`, `en_taller` con acceso de solo lectura para preservar la encapsulación.

### 3.2 Extensibilidad Futura (Módulos Siguientes)
- **`Cliente` & `Mecanico` (Herencia de `Persona`):** Modelado de actores involucrados.
- **`Servicio` & `Repuesto`:** Catálogo de operaciones técnicas y piezas.
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
