"""Tests for the CustodyActor value object."""

import pytest

from forensevision.domain.chain_of_custody.custody_actor import CustodyActor


def test_custody_actor_accepts_valid_values() -> None:
    actor = CustodyActor(
        actor_id="USR-000001",
        name="Investigador Forense",
    )

    assert actor.actor_id == "USR-000001"
    assert actor.name == "Investigador Forense"


def test_custody_actor_rejects_empty_actor_id() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        CustodyActor(
            actor_id="",
            name="Investigador Forense",
        )


def test_custody_actor_rejects_empty_name() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        CustodyActor(
            actor_id="USR-000001",
            name="",
        )


def test_custody_actor_is_immutable() -> None:
    actor = CustodyActor(
        actor_id="USR-000001",
        name="Investigador Forense",
    )

    with pytest.raises(AttributeError):
        actor.name = "Otro actor"  # type: ignore[misc]
