"""Tests for the Evidence aggregate root."""

from forensevision.domain.evidence.evidence import Evidence
from forensevision.domain.evidence.evidence_id import EvidenceId
from forensevision.domain.evidence.evidence_integrity import (
    EvidenceIntegrity,
    HashAlgorithm,
)
from forensevision.domain.evidence.evidence_metadata import EvidenceMetadata
from forensevision.domain.evidence.evidence_source import EvidenceSource
from forensevision.domain.evidence.evidence_type import EvidenceType


def create_evidence(
    evidence_id: str = "EV-000001",
) -> Evidence:
    """Create a valid Evidence instance for testing."""
    return Evidence(
        evidence_id=EvidenceId(evidence_id),
        evidence_type=EvidenceType.IMAGE,
        metadata=EvidenceMetadata(
            filename="evidence.jpg",
            mime_type="image/jpeg",
            size_bytes=1024,
        ),
        source=EvidenceSource("mobile_device"),
        integrity=EvidenceIntegrity(
            algorithm=HashAlgorithm.SHA256,
            value="a" * 64,
        ),
    )


def test_evidence_aggregate_accepts_valid_components() -> None:
    evidence = create_evidence()

    assert evidence.evidence_id == EvidenceId("EV-000001")
    assert evidence.evidence_type is EvidenceType.IMAGE
    assert evidence.metadata.filename == "evidence.jpg"
    assert evidence.source.source == "mobile_device"
    assert evidence.integrity.algorithm is HashAlgorithm.SHA256


def test_evidence_exposes_all_required_components() -> None:
    evidence = create_evidence()

    assert isinstance(evidence.evidence_id, EvidenceId)
    assert isinstance(evidence.evidence_type, EvidenceType)
    assert isinstance(evidence.metadata, EvidenceMetadata)
    assert isinstance(evidence.source, EvidenceSource)
    assert isinstance(evidence.integrity, EvidenceIntegrity)


def test_evidence_identity_is_based_on_evidence_id() -> None:
    first = create_evidence("EV-000001")
    second = create_evidence("EV-000001")

    assert first == second


def test_evidence_with_different_ids_are_not_equal() -> None:
    first = create_evidence("EV-000001")
    second = create_evidence("EV-000002")

    assert first != second


def test_evidence_identity_is_hashable() -> None:
    evidence = create_evidence()

    assert hash(evidence) == hash(EvidenceId("EV-000001"))


def test_evidence_id_is_read_only() -> None:
    evidence = create_evidence()

    try:
        evidence.evidence_id = EvidenceId("EV-000002")  # type: ignore[misc]
    except AttributeError:
        pass
    else:
        raise AssertionError("Evidence identity must be read-only.")


def test_evidence_components_are_value_objects() -> None:
    evidence = create_evidence()

    assert evidence.metadata == EvidenceMetadata(
        filename="evidence.jpg",
        mime_type="image/jpeg",
        size_bytes=1024,
    )

    assert evidence.source == EvidenceSource("mobile_device")

    assert evidence.integrity == EvidenceIntegrity(
        algorithm=HashAlgorithm.SHA256,
        value="a" * 64,
    )
