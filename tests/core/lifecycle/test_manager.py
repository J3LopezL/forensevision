"""
Pruebas unitarias de LifecycleManager.
"""

import pytest

from forensevision.core.lifecycle.exceptions import (
    InvalidLifecycleTransitionError,
)
from forensevision.core.lifecycle.manager import LifecycleManager
from forensevision.core.lifecycle.state import LifecycleState


def test_initial_state_is_created() -> None:
    manager = LifecycleManager()

    assert manager.state is LifecycleState.CREATED


def test_transition_to_initialized() -> None:
    manager = LifecycleManager()

    manager.transition_to(LifecycleState.INITIALIZED)

    assert manager.state is LifecycleState.INITIALIZED


def test_complete_lifecycle() -> None:
    manager = LifecycleManager()

    expected_states = (
        LifecycleState.INITIALIZED,
        LifecycleState.STARTING,
        LifecycleState.RUNNING,
        LifecycleState.STOPPING,
        LifecycleState.STOPPED,
        LifecycleState.DISPOSED,
    )

    for state in expected_states:
        manager.transition_to(state)

    assert manager.state is LifecycleState.DISPOSED


def test_invalid_transition_is_rejected() -> None:
    manager = LifecycleManager()

    with pytest.raises(
        InvalidLifecycleTransitionError
    ):
        manager.transition_to(
            LifecycleState.RUNNING
        )

    assert manager.state is LifecycleState.CREATED


def test_repeated_state_is_rejected() -> None:
    manager = LifecycleManager()

    with pytest.raises(
        InvalidLifecycleTransitionError
    ):
        manager.transition_to(
            LifecycleState.CREATED
        )


def test_disposed_state_is_terminal() -> None:
    manager = LifecycleManager()

    states = (
        LifecycleState.INITIALIZED,
        LifecycleState.STARTING,
        LifecycleState.RUNNING,
        LifecycleState.STOPPING,
        LifecycleState.STOPPED,
        LifecycleState.DISPOSED,
    )

    for state in states:
        manager.transition_to(state)

    with pytest.raises(
        InvalidLifecycleTransitionError
    ):
        manager.transition_to(
            LifecycleState.INITIALIZED
        )

    assert manager.state is LifecycleState.DISPOSED
