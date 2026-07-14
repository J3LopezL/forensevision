"""
Pruebas del registro genérico de componentes.
"""

import pytest

from forensevision.core.registry import Registry


def test_registry_register() -> None:
    registry: Registry[object] = Registry()
    component = object()

    registry.register(
        "component",
        component,
    )

    assert registry.contains("component")


def test_registry_get() -> None:
    registry: Registry[object] = Registry()
    component = object()

    registry.register(
        "component",
        component,
    )

    assert registry.get("component") is component


def test_registry_list() -> None:
    registry: Registry[object] = Registry()

    registry.register("first", object())
    registry.register("second", object())

    assert registry.list() == [
        "first",
        "second",
    ]


def test_registry_replaces_component_with_same_name() -> None:
    registry: Registry[object] = Registry()

    first_component = object()
    second_component = object()

    registry.register(
        "component",
        first_component,
    )

    registry.register(
        "component",
        second_component,
    )

    assert registry.get("component") is second_component


def test_registry_rejects_unknown_component() -> None:
    registry: Registry[object] = Registry()

    with pytest.raises(KeyError):
        registry.get("missing")


def test_registry_preserves_generic_component_type() -> None:
    registry: Registry[str] = Registry()

    registry.register(
        "component",
        "detector",
    )

    component: str = registry.get("component")

    assert component == "detector"
