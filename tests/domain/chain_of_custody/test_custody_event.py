"""Tests for the CustodyEvent value object."""

from datetime import UTC, datetime, timedelta, timezone

import pytest

from forensevision.domain.chain_of_custody.custody_action import CustodyAction
from forensevision.domain.chain_of_custody.custody_actor import CustodyActor
from forensevision.domain.chain_of_custody.custody_event import CustodyEvent
from forensevision.domain.chain_of_custody.custody_event_id import (
    CustodyEventId,
)


def create_event() -> CustodyEvent:
    """Create a valid custody event for testing."""
    return CustodyEvent(
        event_id=CustodyEventId("CUST-000001"),
        evidence_id="EV-000001",
        actor=CustodyActor(
            actor_id="USR-000001",
            name="Investigador Forense",
        ),
        action=CustodyAction.COLLECTION,
        occurred_at=datetime(
            2026,
            7,
            3,
            10,
            30,
            tzinfo=UTC,
        ),
        description="Digital evidence collected from mobile device.",
    )


def test_custody_event_accepts_valid_values() -> None:
    event = create_event()

    assert event.event_id == CustodyEventId("CUST-000001")
    assert event.evidence_id == "EV-000001"
    assert event.actor.actor_id == "USR-000001"
    assert event.action is CustodyAction.COLLECTION
    assert event.description.startswith("Digital evidence")


def test_custody_event_preserves_explicit_timestamp() -> None:
    event = create_event()

    assert event.occurred_at == datetime(
        2026,
        7,
        3,
        10,
        30,
        tzinfo=UTC,
    )


def test_custody_event_normalizes_timestamp_to_utc() -> None:
    event = create_event()

    assert event.occurred_at.tzinfo is UTC
    assert event.occurred_at.utcoffset() == timedelta(0)


def test_custody_event_rejects_naive_timestamp() -> None:
    with pytest.raises(
        ValueError,
        match="must include a timezone",
    ):
        CustodyEvent(
            event_id=CustodyEventId("CUST-000001"),
            evidence_id="EV-000001",
            actor=CustodyActor(
                actor_id="USR-000001",
                name="Investigador Forense",
            ),
            action=CustodyAction.COLLECTION,
            occurred_at=datetime(
                2026,
                7,
                3,
                10,
                30,
            ),
            description="Evidence collected.",
        )


def test_custody_event_rejects_non_utc_timestamp() -> None:
    with pytest.raises(
        ValueError,
        match="must be in UTC",
    ):
        CustodyEvent(
            event_id=CustodyEventId("CUST-000001"),
            evidence_id="EV-000001",
            actor=CustodyActor(
                actor_id="USR-000001",
                name="Investigador Forense",
            ),
            action=CustodyAction.COLLECTION,
            occurred_at=datetime(
                2026,
                7,
                3,
                10,
                30,
                tzinfo=timezone(timedelta(hours=-5)),
            ),
            description="Evidence collected.",
        )


def test_custody_event_rejects_empty_evidence_id() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        CustodyEvent(
            event_id=CustodyEventId("CUST-000001"),
            evidence_id="",
            actor=CustodyActor(
                actor_id="USR-000001",
                name="Investigador Forense",
            ),
            action=CustodyAction.COLLECTION,
            occurred_at=datetime(
                2026,
                7,
                3,
                10,
                30,
                tzinfo=UTC,
            ),
            description="Evidence collected.",
        )


def test_custody_event_rejects_empty_description() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        CustodyEvent(
            event_id=CustodyEventId("CUST-000001"),
            evidence_id="EV-000001",
            actor=CustodyActor(
                actor_id="USR-000001",
                name="Investigador Forense",
            ),
            action=CustodyAction.COLLECTION,
            occurred_at=datetime(
                2026,
                7,
                3,
                10,
                30,
                tzinfo=UTC,
            ),
            description="",
        )


def test_custody_event_is_immutable() -> None:
    event = create_event()

    with pytest.raises(AttributeError):
        event.description = "Modified event"  # type: ignore[misc]
