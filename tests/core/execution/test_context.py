"""
Pruebas del contexto tipado de ejecución.
"""

import pytest

from forensevision.core.execution import (
    ContextKey,
    ContextKeyTypeConflictError,
    ExecutionContext,
)

FRAME_COUNT = ContextKey[int](
    name="frame_count",
    value_type=int,
)

VIDEO_NAME = ContextKey[str](
    name="video_name",
    value_type=str,
)


def test_context_stores_and_resolves_typed_value() -> None:
    context = ExecutionContext()

    context.set(FRAME_COUNT, 120)

    assert context.get(FRAME_COUNT) == 120


def test_context_reports_existing_key() -> None:
    context = ExecutionContext()

    context.set(VIDEO_NAME, "evidence.mp4")

    assert context.contains(VIDEO_NAME) is True


def test_context_reports_missing_key() -> None:
    context = ExecutionContext()

    assert context.contains(VIDEO_NAME) is False


def test_context_raises_key_error_for_missing_value() -> None:
    context = ExecutionContext()

    with pytest.raises(KeyError):
        context.get(VIDEO_NAME)


def test_context_rejects_unexpected_value_type() -> None:
    context = ExecutionContext()

    with pytest.raises(
        TypeError,
        match=(
            "Context value 'frame_count' "
            "is not of type int."
        ),
    ):
        context.set(
            FRAME_COUNT,
            "120",
        )


def test_context_rejects_key_type_conflict_on_set() -> None:
    context = ExecutionContext()

    conflicting_key = ContextKey[str](
        name="frame_count",
        value_type=str,
    )

    context.set(FRAME_COUNT, 120)

    with pytest.raises(
        ContextKeyTypeConflictError,
        match=(
            "Context key 'frame_count' is registered as int "
            "and cannot be used as str."
        ),
    ):
        context.set(
            conflicting_key,
            "120",
        )


def test_context_rejects_key_type_conflict_on_get() -> None:
    context = ExecutionContext()

    conflicting_key = ContextKey[str](
        name="frame_count",
        value_type=str,
    )

    context.set(FRAME_COUNT, 120)

    with pytest.raises(ContextKeyTypeConflictError):
        context.get(conflicting_key)


def test_context_rejects_key_type_conflict_on_contains() -> None:
    context = ExecutionContext()

    conflicting_key = ContextKey[str](
        name="frame_count",
        value_type=str,
    )

    context.set(FRAME_COUNT, 120)

    with pytest.raises(ContextKeyTypeConflictError):
        context.contains(conflicting_key)


def test_context_allows_replacing_value_with_same_key_type() -> None:
    context = ExecutionContext()

    context.set(FRAME_COUNT, 120)
    context.set(FRAME_COUNT, 240)

    assert context.get(FRAME_COUNT) == 240
