"""
Pruebas de gestión de fallos del subsistema Lifecycle.
"""

import pytest

from forensevision.core.lifecycle.exceptions import (
    LifecycleOperationError,
)
from forensevision.core.lifecycle.manager import LifecycleManager
from forensevision.core.lifecycle.state import LifecycleState
from forensevision.interfaces.lifecycle_service import LifecycleService


class FailingService(LifecycleService):
    """
    Servicio configurable para inyectar fallos.
    """

    def __init__(
        self,
        service_name: str,
        failing_operation: str,
    ) -> None:
        self._service_name = service_name
        self._failing_operation = failing_operation

    @property
    def name(self) -> str:
        return self._service_name

    @property
    def version(self) -> str:
        return "0.1.0"

    def initialize(self) -> None:
        self._fail_if_required("initialize")

    def start(self) -> None:
        self._fail_if_required("start")

    def stop(self) -> None:
        self._fail_if_required("stop")

    def dispose(self) -> None:
        self._fail_if_required("dispose")

    def _fail_if_required(
        self,
        operation: str,
    ) -> None:
        if self._failing_operation == operation:
            raise RuntimeError(
                f"Injected failure: {operation}"
            )


def test_initialize_failure_moves_manager_to_failed() -> None:
    manager = LifecycleManager()

    manager.register(
        FailingService(
            "failing-service",
            "initialize",
        )
    )

    with pytest.raises(LifecycleOperationError):
        manager.initialize()

    assert manager.state is LifecycleState.FAILED


def test_start_failure_moves_manager_to_failed() -> None:
    manager = LifecycleManager()

    manager.register(
        FailingService(
            "failing-service",
            "start",
        )
    )

    manager.initialize()

    with pytest.raises(LifecycleOperationError):
        manager.start()

    assert manager.state is LifecycleState.FAILED


def test_stop_failure_moves_manager_to_failed() -> None:
    manager = LifecycleManager()

    manager.register(
        FailingService(
            "failing-service",
            "stop",
        )
    )

    manager.initialize()
    manager.start()

    with pytest.raises(LifecycleOperationError):
        manager.stop()

    assert manager.state is LifecycleState.FAILED


def test_dispose_failure_moves_manager_to_failed() -> None:
    manager = LifecycleManager()

    manager.register(
        FailingService(
            "failing-service",
            "dispose",
        )
    )

    manager.initialize()
    manager.start()
    manager.stop()

    with pytest.raises(LifecycleOperationError):
        manager.dispose()

    assert manager.state is LifecycleState.FAILED


def test_operation_error_identifies_service_and_operation() -> None:
    manager = LifecycleManager()

    manager.register(
        FailingService(
            "model-manager",
            "start",
        )
    )

    manager.initialize()

    with pytest.raises(
        LifecycleOperationError
    ) as exception_info:
        manager.start()

    error = exception_info.value

    assert error.service_name == "model-manager"
    assert error.operation == "start"


def test_operation_error_preserves_original_exception() -> None:
    manager = LifecycleManager()

    manager.register(
        FailingService(
            "gpu-manager",
            "initialize",
        )
    )

    with pytest.raises(
        LifecycleOperationError
    ) as exception_info:
        manager.initialize()

    assert isinstance(
        exception_info.value.__cause__,
        RuntimeError,
    )
