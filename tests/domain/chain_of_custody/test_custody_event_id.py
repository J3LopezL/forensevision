"""Tests for the CustodyEventId value object."""

import pytest

from forensevision.domain.chain_of_custody.custody_event_id import (
    CustodyEventId,
)


def test_custody_event_id_accepts_non_empty_value() -> None:
    event_id = CustodyEventId("CUST-000001")

    assert event_id.value == "CUST-000001"


def test_custody_event_id_rejects_empty_value() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        CustodyEventId("")


def test_custody_event_id_rejects_whitespace_only_value() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        CustodyEventId("   ")


def test_custody_event_id_is_immutable() -> None:
    event_id = CustodyEventId("CUST-000001")

    with pytest.raises(AttributeError):
        event_id.value = "CUST-000002"  # type: ignore[misc]
