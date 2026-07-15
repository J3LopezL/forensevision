"""
Excepciones del Pipeline Execution Kernel.
"""

from __future__ import annotations


class ExecutionError(Exception):
    """
    Excepción base del subsistema de ejecución.
    """


class ContextKeyTypeConflictError(ExecutionError):
    """
    Indica que una identidad de contexto utiliza tipos incompatibles.
    """

    def __init__(
        self,
        key_name: str,
        registered_type: type[object],
        requested_type: type[object],
    ) -> None:
        self.key_name = key_name
        self.registered_type = registered_type
        self.requested_type = requested_type

        super().__init__(
            f"Context key '{key_name}' is registered as "
            f"{registered_type.__name__} and cannot be used as "
            f"{requested_type.__name__}."
        )
