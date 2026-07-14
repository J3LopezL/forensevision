"""
Pruebas unitarias de las excepciones de Lifecycle.
"""

from forensevision.core.lifecycle.exceptions import (
    InvalidLifecycleTransitionError,
    LifecycleError,
)


def test_invalid_transition_is_lifecycle_error() -> None:
    error = InvalidLifecycleTransitionError(
        current_state="created",
        target_state="running",
    )

    assert isinstance(error, LifecycleError)


def test_invalid_transition_preserves_states() -> None:
    error = InvalidLifecycleTransitionError(
        current_state="created",
        target_state="running",
    )

    assert error.current_state == "created"
    assert error.target_state == "running"


def test_invalid_transition_has_descriptive_message() -> None:
    error = InvalidLifecycleTransitionError(
        current_state="created",
        target_state="running",
    )

    assert str(error) == (
        "Transición de ciclo de vida no permitida: "
        "created -> running"
    )
