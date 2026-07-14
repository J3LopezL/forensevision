"""
Pruebas del contenedor de dependencias.
"""

import pytest

from forensevision.core.container import Container


class ExampleService:
    """
    Servicio de prueba para resolución tipada.
    """


class DifferentService:
    """
    Servicio incompatible utilizado en pruebas.
    """


def test_register() -> None:
    container = Container()
    service = ExampleService()

    container.register(
        "service",
        service,
    )

    assert container.contains("service")


def test_resolve() -> None:
    container = Container()
    service = ExampleService()

    container.register(
        "service",
        service,
    )

    resolved_service = container.resolve(
        "service",
        ExampleService,
    )

    assert resolved_service is service


def test_contains() -> None:
    container = Container()

    assert not container.contains("service")

    container.register(
        "service",
        ExampleService(),
    )

    assert container.contains("service")


def test_clear() -> None:
    container = Container()

    container.register(
        "service",
        ExampleService(),
    )

    container.clear()

    assert not container.contains("service")


def test_resolve_rejects_unknown_service() -> None:
    container = Container()

    with pytest.raises(KeyError):
        container.resolve(
            "missing",
            ExampleService,
        )


def test_resolve_rejects_incompatible_type() -> None:
    container = Container()

    container.register(
        "service",
        ExampleService(),
    )

    with pytest.raises(
        TypeError,
        match="Service 'service' is not of type DifferentService",
    ):
        container.resolve(
            "service",
            DifferentService,
        )


def test_resolve_preserves_service_type() -> None:
    container = Container()

    container.register(
        "service",
        ExampleService(),
    )

    service: ExampleService = container.resolve(
        "service",
        ExampleService,
    )

    assert isinstance(service, ExampleService)
