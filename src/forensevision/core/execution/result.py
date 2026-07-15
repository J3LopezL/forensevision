"""
Resultados del Pipeline Execution Kernel.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from forensevision.core.execution.status import StepStatus


@dataclass(frozen=True, slots=True)
class StepResult:
    """
    Resultado inmutable producido por un paso de pipeline.
    """

    step_name: str
    status: StepStatus
    error: Exception | None = None

    @classmethod
    def succeeded(cls, step_name: str) -> StepResult:
        """
        Construye un resultado satisfactorio.
        """

        return cls(
            step_name=step_name,
            status=StepStatus.SUCCEEDED,
        )

    @classmethod
    def failed(
        cls,
        step_name: str,
        error: Exception,
    ) -> StepResult:
        """
        Construye un resultado fallido.
        """

        return cls(
            step_name=step_name,
            status=StepStatus.FAILED,
            error=error,
        )

    @classmethod
    def skipped(cls, step_name: str) -> StepResult:
        """
        Construye un resultado omitido.
        """

        return cls(
            step_name=step_name,
            status=StepStatus.SKIPPED,
        )


@dataclass(frozen=True, slots=True)
class PipelineResult:
    """
    Resultado agregado de una ejecución de pipeline.
    """

    steps: tuple[StepResult, ...] = field(default_factory=tuple)

    @property
    def succeeded(self) -> bool:
        """
        Indica si todos los pasos terminaron satisfactoriamente.
        """

        return all(
            step.status is StepStatus.SUCCEEDED
            for step in self.steps
        )

    @property
    def failed(self) -> bool:
        """
        Indica si existe al menos un paso fallido.
        """

        return any(
            step.status is StepStatus.FAILED
            for step in self.steps
        )
