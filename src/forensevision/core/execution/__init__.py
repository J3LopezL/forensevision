"""
Modelo de ejecución del Pipeline Kernel.
"""

from forensevision.core.execution.context import ContextKey, ExecutionContext
from forensevision.core.execution.exceptions import (
    ContextKeyTypeConflictError,
    ExecutionError,
)
from forensevision.core.execution.executor import SequentialExecutor
from forensevision.core.execution.pipeline import Pipeline
from forensevision.core.execution.result import PipelineResult, StepResult
from forensevision.core.execution.status import StepStatus
from forensevision.core.execution.step import PipelineStep

__all__ = [
    "ContextKey",
    "ContextKeyTypeConflictError",
    "ExecutionContext",
    "ExecutionError",
    "Pipeline",
    "PipelineResult",
    "PipelineStep",
    "SequentialExecutor",
    "StepResult",
    "StepStatus",
]
