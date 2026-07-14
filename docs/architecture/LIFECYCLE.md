# Lifecycle del Framework

Todos los servicios del Framework seguirán el mismo ciclo de vida.

---

## Estados

CREATED

↓

INITIALIZED

↓

STARTING

↓

RUNNING

↓

STOPPING

↓

STOPPED

↓

DISPOSED

---

## Descripción

### CREATED

El objeto existe pero todavía no posee recursos.

### INITIALIZED

Se cargó la configuración.

Todavía no utiliza recursos externos.

### STARTING

Se inicializan recursos.

Ejemplos:

- GPU
- Modelos IA
- OCR
- API
- Plugins

### RUNNING

Servicio operativo.

### STOPPING

Liberación ordenada.

### STOPPED

Servicio detenido.

### DISPOSED

Todos los recursos fueron liberados.
