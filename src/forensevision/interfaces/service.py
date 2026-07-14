"""
Contrato base de los servicios de ForenseVisión.
"""

from __future__ import annotations

from abc import abstractmethod

from forensevision.interfaces.component import Component


class Service(Component):
    """
    Contrato base para servicios inicializables.
    """

    @abstractmethod
    def initialize(self) -> None:
        """
        Inicializa el servicio.
        """
        ...
