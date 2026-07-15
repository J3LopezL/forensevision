"""
Contrato de pasos ejecutables del Pipeline Kernel.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from forensevision.core.execution.context import ExecutionContext


class PipelineStep(ABC):
    """
    Define una unidad de procesamiento ejecutable.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Obtiene la identidad lógica del paso.
        """

        ...

    @abstractmethod
    def execute(
        self,
        context: ExecutionContext,
    ) -> None:
        """
        Ejecuta el paso utilizando el contexto compartido.
        """

        ...
