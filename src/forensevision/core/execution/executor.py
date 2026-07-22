"""
Ejecutores del Pipeline Execution Kernel.
"""

from __future__ import annotations

from forensevision.core.execution.configuration import (
    ExecutorConfiguration,
)
from forensevision.core.execution.context import ExecutionContext
from forensevision.core.execution.executor_contract import (
    PipelineExecutor,
)
from forensevision.core.execution.pipeline import Pipeline
from forensevision.core.execution.result import PipelineResult, StepResult


class SequentialExecutor(PipelineExecutor):
    """
    Ejecuta los pasos de un pipeline secuencialmente.
    """

    def __init__(
        self,
        configuration: ExecutorConfiguration | None = None,
    ) -> None:
        self._configuration = (
            configuration
            if configuration is not None
            else ExecutorConfiguration()
        )

    def execute(
        self,
        pipeline: Pipeline,
        context: ExecutionContext,
    ) -> PipelineResult:
        """
        Ejecuta un pipeline sobre el contexto suministrado.
        """

        results: list[StepResult] = []
        stop_execution = False

        for step in pipeline:
            if stop_execution:
                results.append(
                    StepResult.skipped(step.name)
                )
                continue

            try:
                step.execute(context)
            except Exception as error:
                results.append(
                    StepResult.failed(
                        step.name,
                        error,
                    )
                )
                if self._configuration.fail_fast:
                    stop_execution = True
            else:
                results.append(
                    StepResult.succeeded(step.name)
                )

        return PipelineResult(
            steps=tuple(results),
        )
