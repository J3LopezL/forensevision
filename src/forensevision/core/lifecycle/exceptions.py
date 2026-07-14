"""
Excepciones del subsistema Lifecycle.
"""

from __future__ import annotations


class LifecycleError(RuntimeError):
    """
    Error base del subsistema Lifecycle.
    """


class InvalidLifecycleTransitionError(LifecycleError):
    """
    Indica una transición de estado no permitida.
    """

    def __init__(
        self,
        current_state: str,
        target_state: str,
    ) -> None:
        self.current_state = current_state
        self.target_state = target_state

        message = (
            "Transición de ciclo de vida no permitida: "
            f"{current_state} -> {target_state}"
        )

        super().__init__(message)


class LifecycleOperationError(LifecycleError):
    """
    Indica un fallo durante una operación sobre un servicio.
    """

    def __init__(
        self,
        operation: str,
        service_name: str,
    ) -> None:
        self.operation = operation
        self.service_name = service_name

        message = (
            "Error durante la operación Lifecycle "
            f"'{operation}' del servicio '{service_name}'."
        )

        super().__init__(message)
