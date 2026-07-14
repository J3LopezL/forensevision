"""
Estados del ciclo de vida de los componentes de ForenseVisión.
"""

from __future__ import annotations

from enum import StrEnum


class LifecycleState(StrEnum):
    """
    Estados válidos del ciclo de vida de un componente.
    """

    CREATED = "created"
    INITIALIZED = "initialized"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"
    DISPOSED = "disposed"
    FAILED = "failed"
