"""Tests for the ChainOfCustody aggregate root."""

from datetime import UTC, datetime, timedelta

import pytest

from forensevision.domain.chain_of_custody.chain_of_custody import (
    ChainOfCustody,
)
from forensevision.domain.chain_of_custody.chain_of_custody_id import (
    ChainOfCustodyId,
)
from forensevision.domain.chain_of_custody.custody_action import CustodyAction
from forensevision.domain.chain_of_custody.custody_actor import CustodyActor
from forensevision.domain.chain_of_custody.custody_event import CustodyEvent
from forensevision.domain.chain_of_custody.custody_event_id import (
    CustodyEventId,
)
from forensevision.domain.chain_of_custody.exceptions import (
    CustodyEventChronologyError,
    CustodyEvidenceMismatchError,
)

BASE_TIME = datetime(2026, 7, 3, 10, 0, tzinfo=UTC)


def create_event(
    event_id: str = "CUST-000001",
    evidence_id: str = "EV-000001",
    occurred_at: datetime = BASE_TIME,
) -> CustodyEvent:
    """Create a valid custody event for testing."""
    return CustodyEvent(
        event_id=CustodyEventId(event_id),
        evidence_id=evidence_id,
        actor=CustodyActor(
            actor_id="USR-000001",
            name="Investigador Forense",
        ),
        action=CustodyAction.COLLECTION,
        occurred_at=occurred_at,
        description="Digital evidence custody action.",
    )


def create_chain(
    chain_id: str = "CHAIN-000001",
    evidence_id: str = "EV-000001",
) -> ChainOfCustody:
    """Create a valid chain of custody for testing."""
    return ChainOfCustody(
        chain_id=ChainOfCustodyId(chain_id),
        evidence_id=evidence_id,
    )


def test_chain_of_custody_accepts_valid_values() -> None:
    chain = create_chain()

    assert chain.chain_id == ChainOfCustodyId("CHAIN-000001")
    assert chain.evidence_id == "EV-000001"
    assert chain.events == ()
    assert chain.last_event_at is None


def test_chain_of_custody_rejects_empty_evidence_id() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        create_chain(evidence_id="")


def test_chain_of_custody_identity_is_based_on_chain_id() -> None:
    first = create_chain("CHAIN-000001", "EV-000001")
    second = create_chain("CHAIN-000001", "EV-000002")

    assert first == second


def test_chain_of_custody_identity_is_hashable() -> None:
    chain = create_chain()

    assert hash(chain) == hash(ChainOfCustodyId("CHAIN-000001"))


def test_chain_of_custody_properties_are_read_only() -> None:
    chain = create_chain()

    with pytest.raises(AttributeError):
        chain.chain_id = ChainOfCustodyId("CHAIN-000002")  # type: ignore[misc]

    with pytest.raises(AttributeError):
        chain.evidence_id = "EV-000002"  # type: ignore[misc]


def test_chain_starts_without_events() -> None:
    chain = create_chain()

    assert chain.events == ()
    assert chain.last_event_at is None


def test_chain_can_add_event() -> None:
    chain = create_chain()
    event = create_event()

    chain.add_event(event)

    assert chain.events == (event,)
    assert chain.last_event_at == BASE_TIME


def test_chain_preserves_event_order() -> None:
    chain = create_chain()

    first = create_event(
        event_id="CUST-000001",
        occurred_at=BASE_TIME,
    )
    second = create_event(
        event_id="CUST-000002",
        occurred_at=BASE_TIME + timedelta(minutes=30),
    )

    chain.add_event(first)
    chain.add_event(second)

    assert chain.events == (first, second)


def test_chain_rejects_event_from_another_evidence() -> None:
    chain = create_chain(evidence_id="EV-000001")
    event = create_event(evidence_id="EV-000002")

    with pytest.raises(
        CustodyEvidenceMismatchError,
        match="does not match",
    ):
        chain.add_event(event)

    assert chain.events == ()


def test_chain_rejects_event_before_last_event() -> None:
    chain = create_chain()

    first = create_event(
        event_id="CUST-000001",
        occurred_at=BASE_TIME,
    )
    earlier = create_event(
        event_id="CUST-000002",
        occurred_at=BASE_TIME - timedelta(minutes=1),
    )

    chain.add_event(first)

    with pytest.raises(
        CustodyEventChronologyError,
        match="cannot be earlier",
    ):
        chain.add_event(earlier)

    assert chain.events == (first,)


def test_chain_accepts_events_with_same_timestamp() -> None:
    chain = create_chain()

    first = create_event(
        event_id="CUST-000001",
        occurred_at=BASE_TIME,
    )
    second = create_event(
        event_id="CUST-000002",
        occurred_at=BASE_TIME,
    )

    chain.add_event(first)
    chain.add_event(second)

    assert chain.events == (first, second)


def test_chain_events_are_exposed_as_immutable_sequence() -> None:
    chain = create_chain()
    event = create_event()

    chain.add_event(event)

    events = chain.events

    assert isinstance(events, tuple)
    assert events == (event,)
