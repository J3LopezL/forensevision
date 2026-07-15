"""
Ejecutores del Pipeline Execution Kernel.
"""

from __future__ import annotations

from forensevision.core.execution.context import ExecutionContext
from forensevision.core.execution.pipeline import Pipeline
from forensevision.core.execution.result import PipelineResult, StepResult


class SequentialExecutor:
    """
    Ejecuta los pasos de un pipeline secuencialmente.

    La política de ejecución es fail-fast: después del primer
    fallo, los pasos restantes se registran como omitidos.
    """

    def execute(
        self,
        pipeline: Pipeline,
        context: ExecutionContext,
    ) -> PipelineResult:
        """
        Ejecuta un pipeline sobre el contexto suministrado.
        """

        results: list[StepResult] = []
        failed = False

        for step in pipeline:
            if failed:
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
                failed = True
            else:
                results.append(
                    StepResult.succeeded(step.name)
                )

        return PipelineResult(
            steps=tuple(results),
        )
