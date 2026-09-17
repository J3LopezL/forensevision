"""Tests for the EvidenceId value object."""

import pytest

from forensevision.domain.evidence.evidence_id import EvidenceId


def test_evidence_id_accepts_non_empty_value() -> None:
    evidence_id = EvidenceId("EV-000001")

    assert evidence_id.value == "EV-000001"


def test_evidence_id_rejects_empty_value() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        EvidenceId("")


def test_evidence_id_rejects_whitespace_only_value() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        EvidenceId("   ")


def test_evidence_id_equality_is_based_on_value() -> None:
    first = EvidenceId("EV-000001")
    second = EvidenceId("EV-000001")

    assert first == second


def test_evidence_id_is_immutable() -> None:
    evidence_id = EvidenceId("EV-000001")

    with pytest.raises(AttributeError):
        evidence_id.value = "EV-000002"  # type: ignore[misc]
