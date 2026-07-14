# ADR-0002: Contrato de servicios administrados por Lifecycle

## Estado

Aceptado

## Contexto

El contrato `Service` de ForenseVisión define únicamente la operación
`initialize()`.

El subsistema Lifecycle establece un ciclo de vida compuesto por los estados:

- CREATED
- INITIALIZED
- STARTING
- RUNNING
- STOPPING
- STOPPED
- DISPOSED

No todos los servicios del Framework administran recursos externos ni
requieren operaciones de inicio, detención y liberación.

Extender `Service` con todas las operaciones del ciclo de vida obligaría a
servicios simples a implementar métodos que no necesitan.

## Decisión

Se mantendrá `Service` como contrato mínimo de inicialización.

Se creará el contrato `LifecycleService` como especialización de `Service`.

`LifecycleService` definirá las operaciones:

- initialize()
- start()
- stop()
- dispose()

Los servicios que administren recursos deberán implementar
`LifecycleService`.

## Consecuencias

### Positivas

- Aplicación del Interface Segregation Principle.
- Contratos explícitos.
- Menor acoplamiento.
- Servicios simples permanecen simples.
- Lifecycle puede administrar únicamente componentes compatibles.

### Negativas

- Se incorpora una interfaz adicional.
- Los desarrolladores deberán seleccionar correctamente el contrato del servicio.

## Regla arquitectónica

Todo servicio que administre recursos externos, procesos de larga duración
o recursos que requieran liberación deberá implementar `LifecycleService`.
