"""
Contrato para servicios administrados por Lifecycle.
"""

from __future__ import annotations

from abc import abstractmethod

from forensevision.interfaces.service import Service


class LifecycleService(Service):
    """
    Contrato de un servicio con ciclo de vida administrado.
    """

    @abstractmethod
    def start(self) -> None:
        """
        Inicia los recursos administrados por el servicio.
        """
        ...

    @abstractmethod
    def stop(self) -> None:
        """
        Detiene ordenadamente el servicio.
        """
        ...

    @abstractmethod
    def dispose(self) -> None:
        """
        Libera definitivamente los recursos del servicio.
        """
        ...
