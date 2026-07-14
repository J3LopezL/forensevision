# Arquitectura del Kernel

```text
                Application
                      │
                      ▼
                Bootstrap
                      │
                      ▼
           ApplicationContext
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
 Configuration    Container     Registry
        │
        ▼
     Logger

```
