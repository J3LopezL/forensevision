"""
Pruebas de compensación ante fallos parciales de Lifecycle.
"""

import pytest

from forensevision.core.lifecycle.exceptions import (
    LifecycleOperationError,
)
from forensevision.core.lifecycle.manager import LifecycleManager
from forensevision.core.lifecycle.state import LifecycleState
from forensevision.interfaces.lifecycle_service import LifecycleService


class CompensableService(LifecycleService):
    """
    Servicio de prueba con registro de operaciones y fallos configurables.
    """

    def __init__(
        self,
        service_name: str,
        events: list[str],
        failing_operation: str | None = None,
    ) -> None:
        self._service_name = service_name
        self._events = events
        self._failing_operation = failing_operation

    @property
    def name(self) -> str:
        return self._service_name

    @property
    def version(self) -> str:
        return "0.1.0"

    def initialize(self) -> None:
        self._record_and_fail_if_required("initialize")

    def start(self) -> None:
        self._record_and_fail_if_required("start")

    def stop(self) -> None:
        self._record_and_fail_if_required("stop")

    def dispose(self) -> None:
        self._record_and_fail_if_required("dispose")

    def _record_and_fail_if_required(
        self,
        operation: str,
    ) -> None:
        self._events.append(
            f"{self.name}:{operation}"
        )

        if self._failing_operation == operation:
            raise RuntimeError(
                f"Injected failure: {operation}"
            )


def test_initialize_failure_disposes_completed_services_in_reverse_order() -> None:
    events: list[str] = []
    manager = LifecycleManager()

    manager.register(
        CompensableService("a", events)
    )
    manager.register(
        CompensableService("b", events)
    )
    manager.register(
        CompensableService(
            "c",
            events,
            failing_operation="initialize",
        )
    )

    with pytest.raises(LifecycleOperationError):
        manager.initialize()

    assert events == [
        "a:initialize",
        "b:initialize",
        "c:initialize",
        "b:dispose",
        "a:dispose",
    ]

    assert manager.state is LifecycleState.FAILED


def test_initialize_failure_does_not_compensate_failing_service() -> None:
    events: list[str] = []
    manager = LifecycleManager()

    manager.register(
        CompensableService(
            "a",
            events,
            failing_operation="initialize",
        )
    )

    with pytest.raises(LifecycleOperationError):
        manager.initialize()

    assert events == [
        "a:initialize",
    ]


def test_start_failure_stops_started_services_in_reverse_order() -> None:
    events: list[str] = []
    manager = LifecycleManager()

    manager.register(
        CompensableService("a", events)
    )
    manager.register(
        CompensableService("b", events)
    )
    manager.register(
        CompensableService(
            "c",
            events,
            failing_operation="start",
        )
    )

    manager.initialize()
    events.clear()

    with pytest.raises(LifecycleOperationError):
        manager.start()

    assert events == [
        "a:start",
        "b:start",
        "c:start",
        "b:stop",
        "a:stop",
    ]

    assert manager.state is LifecycleState.FAILED


def test_start_failure_does_not_compensate_failing_service() -> None:
    events: list[str] = []
    manager = LifecycleManager()

    manager.register(
        CompensableService(
            "a",
            events,
            failing_operation="start",
        )
    )

    manager.initialize()
    events.clear()

    with pytest.raises(LifecycleOperationError):
        manager.start()

    assert events == [
        "a:start",
    ]


def test_compensation_failure_does_not_hide_primary_failure() -> None:
    events: list[str] = []
    manager = LifecycleManager()

    manager.register(
        CompensableService(
            "a",
            events,
            failing_operation="dispose",
        )
    )
    manager.register(
        CompensableService(
            "b",
            events,
            failing_operation="initialize",
        )
    )

    with pytest.raises(
        LifecycleOperationError
    ) as exception_info:
        manager.initialize()

    error = exception_info.value

    assert error.service_name == "b"
    assert error.operation == "initialize"

    assert isinstance(
        error.__cause__,
        RuntimeError,
    )

    assert events == [
        "a:initialize",
        "b:initialize",
        "a:dispose",
    ]

    assert manager.state is LifecycleState.FAILED
