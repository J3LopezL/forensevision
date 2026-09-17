"""Tests for EvidenceStatus."""

from forensevision.domain.evidence.evidence_status import EvidenceStatus


def test_evidence_status_contains_expected_values() -> None:
    assert EvidenceStatus.REGISTERED.value == "registered"
    assert EvidenceStatus.PRESERVED.value == "preserved"
    assert EvidenceStatus.PROCESSED.value == "processed"
    assert EvidenceStatus.ANALYZED.value == "analyzed"
    assert EvidenceStatus.ARCHIVED.value == "archived"


def test_evidence_status_is_string_compatible() -> None:
    assert isinstance(EvidenceStatus.REGISTERED, str)
    assert EvidenceStatus.REGISTERED == "registered"


def test_evidence_status_members_are_distinct() -> None:
    statuses = list(EvidenceStatus)

    assert len(statuses) == 5
    assert len(set(statuses)) == 5
