"""
Configuración de los ejecutores del Pipeline Kernel.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ExecutorConfiguration:
    """
    Configuración base de un ejecutor.
    """

    fail_fast: bool = True
