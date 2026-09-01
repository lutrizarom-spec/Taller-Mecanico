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
│   └── vehiculo.py        # Clase Vehiculo con encapsulación y métodos de estado
├── tests/
│   ├── __init__.py
│   └── test_vehiculo.py   # Suite de pruebas unitarias (unittest)
├── docs/
│   ├── README.md
│   └── DESIGN.md          # Especificación de diseño y arquitectura
├── .gitignore             # Configuración de exclusiones Git
├── main.py                # Simulación integral del flujo de taller
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
- **Suite de Pruebas:** Implementación de `tests/test_vehiculo.py` con 6 casos de prueba automatizados.
- **Documentación de Arquitectura:** Creación de `docs/DESIGN.md` detallando el modelo de dominio.
