"""
Políticas de ejecución del Pipeline Execution Kernel.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from forensevision.core.execution.result import StepResult
from forensevision.core.execution.status import StepStatus


class ExecutionPolicy(ABC):
    """
    Define cómo reacciona el ejecutor después de cada paso.
    """

    @abstractmethod
    def should_continue(
        self,
        result: StepResult,
    ) -> bool:
        """
        Indica si la ejecución debe continuar.
        """

class FailFastPolicy(ExecutionPolicy):
    """
    Detiene la ejecución después del primer fallo.
    """

    def should_continue(
        self,
        result: StepResult,
    ) -> bool:
        return result.status is StepStatus.SUCCEEDED
