Decisiones de Arquitectura
ADR-0001 – Arquitectura Hexagonal (Ports and Adapters), cada archivo tendrá una única responsabilidad (SRP - Single Responsibility Principle)
ADR-0002 - Ninguna ruta absoluta o relativa podrá escribirse directamente en el código del framework. Todas las rutas deberán obtenerse a través de Paths.
ADR-0003 - Nunca usar print(), Los print() desaparecerán del proyecto. Todo deberá pasar por el servicio: Logger
ADR-0004 - Introducción del concepto de Bootstrap.(Configuration, Logger, Registry, (futuro) ModelManager, PluginManager, Pipeline.
ADR-0005 - Todo servicio del Framework deberá implementar una interfaz.
ADR-0006 - No seguir utilizando Singleton (dificulta las pruebas unitarias, aumenta el acoplamiento, dificulta ejecutar varios pipelines simultáneamente, complica el procesamiento distribuido) se empleará Dependency Injection.
ADR-0007 - Todo componente del Framework heredará de Component.

