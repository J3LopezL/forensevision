"""
Pruebas unitarias de LifecycleState.
"""

from forensevision.core.lifecycle.state import LifecycleState


def test_lifecycle_state_contains_expected_states() -> None:
    expected_states = {
        "created",
        "initialized",
        "starting",
        "running",
        "stopping",
        "stopped",
        "disposed",
        "failed",
    }

    actual_states = {
        state.value
        for state in LifecycleState
    }

    assert actual_states == expected_states


def test_lifecycle_state_is_string_compatible() -> None:
    assert LifecycleState.CREATED == "created"
    assert LifecycleState.RUNNING == "running"
    assert LifecycleState.DISPOSED == "disposed"
    assert LifecycleState.FAILED == "failed"
