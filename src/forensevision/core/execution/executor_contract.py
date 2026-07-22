"""
Contrato para ejecutores de Pipeline.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from forensevision.core.execution.context import ExecutionContext
from forensevision.core.execution.pipeline import Pipeline
from forensevision.core.execution.result import PipelineResult


class PipelineExecutor(ABC):
    """
    Contrato para cualquier estrategia de ejecución de Pipeline.
    """

    @abstractmethod
    def execute(
        self,
        pipeline: Pipeline,
        context: ExecutionContext,
    ) -> PipelineResult:
        """
        Ejecuta un pipeline utilizando una política determinada.
        """
