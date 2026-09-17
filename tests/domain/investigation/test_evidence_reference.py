"""Tests for the EvidenceReference value object."""

import pytest

from forensevision.domain.investigation.evidence_reference import (
    EvidenceReference,
)


def test_evidence_reference_accepts_non_empty_id() -> None:
    reference = EvidenceReference("EV-000001")

    assert reference.evidence_id == "EV-000001"


def test_evidence_reference_rejects_empty_id() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        EvidenceReference("")


def test_evidence_reference_rejects_whitespace_only_id() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        EvidenceReference("   ")


def test_evidence_reference_equality_is_based_on_evidence_id() -> None:
    first = EvidenceReference("EV-000001")
    second = EvidenceReference("EV-000001")

    assert first == second


def test_evidence_references_with_different_ids_are_not_equal() -> None:
    first = EvidenceReference("EV-000001")
    second = EvidenceReference("EV-000002")

    assert first != second


def test_evidence_reference_is_immutable() -> None:
    reference = EvidenceReference("EV-000001")

    with pytest.raises(AttributeError):
        reference.evidence_id = "EV-000002"  # type: ignore[misc]
