"""
Contrato base para todos los servicios del Framework.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class Service(ABC):
    """
    Interfaz base de cualquier servicio.
    """

    @abstractmethod
    def initialize(self) -> None:
        """
        Inicializa el servicio.
        """
        raise NotImplementedError()
