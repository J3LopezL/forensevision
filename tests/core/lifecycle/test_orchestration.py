"""
Pruebas de orquestación del subsistema Lifecycle.
"""

import pytest

from forensevision.core.lifecycle.manager import LifecycleManager
from forensevision.interfaces.lifecycle_service import LifecycleService


class RecordingService(LifecycleService):
    """
    Servicio de prueba que registra las operaciones ejecutadas.
    """

    def __init__(
        self,
        service_name: str,
        events: list[str],
    ) -> None:
        self._service_name = service_name
        self._events = events

    @property
    def name(self) -> str:
        return self._service_name

    @property
    def version(self) -> str:
        return "0.1.0"

    def initialize(self) -> None:
        self._events.append(
            f"{self.name}:initialize"
        )

    def start(self) -> None:
        self._events.append(
            f"{self.name}:start"
        )

    def stop(self) -> None:
        self._events.append(
            f"{self.name}:stop"
        )

    def dispose(self) -> None:
        self._events.append(
            f"{self.name}:dispose"
        )


def test_register_lifecycle_service() -> None:
    manager = LifecycleManager()
    events: list[str] = []

    service = RecordingService(
        "service-a",
        events,
    )

    manager.register(service)

    assert manager.services == (service,)


def test_duplicate_service_name_is_rejected() -> None:
    manager = LifecycleManager()
    events: list[str] = []

    manager.register(
        RecordingService(
            "service-a",
            events,
        )
    )

    with pytest.raises(ValueError):
        manager.register(
            RecordingService(
                "service-a",
                events,
            )
        )


def test_initialize_preserves_registration_order() -> None:
    manager = LifecycleManager()
    events: list[str] = []

    manager.register(
        RecordingService("a", events)
    )
    manager.register(
        RecordingService("b", events)
    )
    manager.register(
        RecordingService("c", events)
    )

    manager.initialize()

    assert events == [
        "a:initialize",
        "b:initialize",
        "c:initialize",
    ]


def test_start_preserves_registration_order() -> None:
    manager = LifecycleManager()
    events: list[str] = []

    manager.register(
        RecordingService("a", events)
    )
    manager.register(
        RecordingService("b", events)
    )
    manager.register(
        RecordingService("c", events)
    )

    manager.initialize()
    events.clear()

    manager.start()

    assert events == [
        "a:start",
        "b:start",
        "c:start",
    ]


def test_stop_uses_reverse_registration_order() -> None:
    manager = LifecycleManager()
    events: list[str] = []

    manager.register(
        RecordingService("a", events)
    )
    manager.register(
        RecordingService("b", events)
    )
    manager.register(
        RecordingService("c", events)
    )

    manager.initialize()
    manager.start()
    events.clear()

    manager.stop()

    assert events == [
        "c:stop",
        "b:stop",
        "a:stop",
    ]


def test_dispose_uses_reverse_registration_order() -> None:
    manager = LifecycleManager()
    events: list[str] = []

    manager.register(
        RecordingService("a", events)
    )
    manager.register(
        RecordingService("b", events)
    )
    manager.register(
        RecordingService("c", events)
    )

    manager.initialize()
    manager.start()
    manager.stop()
    events.clear()

    manager.dispose()

    assert events == [
        "c:dispose",
        "b:dispose",
        "a:dispose",
    ]
