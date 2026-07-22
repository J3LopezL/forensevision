"""
Contratos para los reportes de ejecución.
"""

from __future__ import annotations

from forensevision.core.execution.result import PipelineResult


class ExecutionReport:
    """
    Contrato base para cualquier reporte de ejecución.
    """


class StandardExecutionReport(ExecutionReport):
    """
    Reporte estándar del Pipeline Execution Kernel.
    """

    def __init__(
        self,
        result: PipelineResult,
    ) -> None:
        self.result = result
