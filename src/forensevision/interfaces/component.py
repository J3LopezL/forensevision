"""
Contrato base de los componentes de ForenseVisión.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Component(ABC):
    """
    Contrato base para componentes identificables del Framework.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Obtiene el nombre lógico único del componente.
        """
        ...

    @property
    @abstractmethod
    def version(self) -> str:
        """
        Obtiene la versión del componente.
        """
        ...
