# Kernel de ForenseVisión

## Objetivo

El Kernel constituye el núcleo estable del Framework.

Su responsabilidad es iniciar, coordinar y administrar el ciclo de vida de la plataforma.

El Kernel nunca contendrá lógica de visión artificial ni algoritmos forenses.

---

## Responsabilidades

- Inicialización del Framework.
- Configuración.
- Registro de componentes.
- Contenedor de dependencias.
- Ciclo de vida.
- Eventos.
- Logging.
- Contexto.
- Gestión de Plugins.

---

## Restricciones

El Kernel NO conocerá:

- OpenCV
- TensorFlow
- PyTorch
- MediaPipe
- OCR
- Detectores
- Reportes
- Evidencias
- IA

Todas esas capacidades pertenecerán a otros dominios.
