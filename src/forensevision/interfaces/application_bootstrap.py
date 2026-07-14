"""
Contrato de inicialización de la aplicación.
"""

from __future__ import annotations

from typing import Protocol

from forensevision.core.application_context import ApplicationContext


class ApplicationBootstrap(Protocol):
    """
    Contrato requerido para inicializar Application.
    """

    def initialize(self) -> ApplicationContext:
        """
        Construye el contexto de ejecución.
        """
        ...
