# Patrón Arquitectónico

## Arquitectura Oficial

ForenseVisión adopta una arquitectura híbrida compuesta por:

- Clean Architecture
- Hexagonal Architecture
- Microkernel Architecture

---

## Clean Architecture

Define las dependencias.

El dominio nunca dependerá de tecnologías.

---

## Hexagonal

Toda integración externa se realizará mediante puertos y adaptadores.

Ejemplos:

- OpenCV
- TensorFlow
- PyTorch
- MediaPipe
- PostgreSQL

---

## Microkernel

El Kernel del Framework permanecerá pequeño.

Toda nueva funcionalidad se implementará como un módulo o plugin.
