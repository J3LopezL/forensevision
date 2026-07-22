"""
Pruebas del contrato LifecycleService.
"""

import pytest

from forensevision.interfaces.lifecycle_service import (
    LifecycleService,
)


class IncompleteLifecycleService(LifecycleService):
    """
    Implementación deliberadamente incompleta.
    """


class CompleteLifecycleService(LifecycleService):
    """
    Implementación mínima válida para pruebas.
    """

    @property
    def name(self) -> str:
        return "TestLifecycleService"

    @property
    def version(self) -> str:
        return "0.1.0"

    def initialize(self) -> None:
        pass

    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass

    def dispose(self) -> None:
        pass


def test_incomplete_lifecycle_service_cannot_be_instantiated() -> None:
    with pytest.raises(TypeError):
        IncompleteLifecycleService()  # type: ignore[abstract]


def test_complete_lifecycle_service_can_be_instantiated() -> None:
    service = CompleteLifecycleService()

    assert isinstance(service, LifecycleService)


def test_lifecycle_service_preserves_component_identity() -> None:
    service = CompleteLifecycleService()

    assert service.name == "TestLifecycleService"
    assert service.version == "0.1.0"
