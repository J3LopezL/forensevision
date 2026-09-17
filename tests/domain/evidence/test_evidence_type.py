"""Tests for the EvidenceType enumeration."""

from forensevision.domain.evidence.evidence_type import EvidenceType


def test_evidence_type_contains_expected_values() -> None:
    assert EvidenceType.FILE.value == "file"
    assert EvidenceType.IMAGE.value == "image"
    assert EvidenceType.VIDEO.value == "video"
    assert EvidenceType.AUDIO.value == "audio"
    assert EvidenceType.EMAIL.value == "email"
    assert EvidenceType.NETWORK_CAPTURE.value == "network_capture"
    assert EvidenceType.DATABASE.value == "database"
    assert EvidenceType.LOG.value == "log"
    assert EvidenceType.OTHER.value == "other"


def test_evidence_type_is_string_compatible() -> None:
    evidence_type = EvidenceType.IMAGE

    assert isinstance(evidence_type, str)
    assert evidence_type.value == "image"


def test_evidence_type_members_are_distinct() -> None:
    evidence_types = list(EvidenceType)

    assert len(evidence_types) == len(set(evidence_types))
