"""
Contrato base para cualquier componente del Framework.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class Component(ABC):
    """
    Todo componente del Framework debe proporcionar
    información básica sobre sí mismo.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Nombre del componente."""

    @property
    @abstractmethod
    def version(self) -> str:
        """Versión del componente."""
