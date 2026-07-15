"""
Estados de ejecución del Pipeline Kernel.
"""

from __future__ import annotations

from enum import StrEnum


class StepStatus(StrEnum):
    """
    Representa el estado terminal de un paso de pipeline.
    """

    SUCCEEDED = "succeeded"
    FAILED = "failed"
    SKIPPED = "skipped"
