"""Tests for Evidence aggregate invariants."""

import pytest

from forensevision.domain.evidence.evidence import Evidence
from forensevision.domain.evidence.evidence_id import EvidenceId
from forensevision.domain.evidence.evidence_integrity import (
    EvidenceIntegrity,
    HashAlgorithm,
)
from forensevision.domain.evidence.evidence_metadata import EvidenceMetadata
from forensevision.domain.evidence.evidence_source import EvidenceSource
from forensevision.domain.evidence.evidence_status import EvidenceStatus
from forensevision.domain.evidence.evidence_type import EvidenceType


def create_evidence() -> Evidence:
    """Create a valid Evidence instance for invariant tests."""
    return Evidence(
        evidence_id=EvidenceId("EV-000001"),
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


def test_evidence_initial_status_is_registered() -> None:
    evidence = create_evidence()

    assert evidence.status is EvidenceStatus.REGISTERED


def test_evidence_identity_is_defined_by_evidence_id() -> None:
    first = create_evidence()
    second = create_evidence()

    assert first.evidence_id == second.evidence_id
    assert first == second


def test_evidence_identity_remains_hashable() -> None:
    evidence = create_evidence()

    assert hash(evidence) == hash(evidence.evidence_id)


def test_evidence_components_are_read_only() -> None:
    evidence = create_evidence()

    with pytest.raises(AttributeError):
        evidence.evidence_id = EvidenceId("EV-000002")  # type: ignore[misc]

    with pytest.raises(AttributeError):
        evidence.status = EvidenceStatus.ANALYZED  # type: ignore[misc]


def test_evidence_lifecycle_is_modified_only_through_domain_behavior() -> None:
    evidence = create_evidence()

    assert evidence.status is EvidenceStatus.REGISTERED

    evidence.preserve()

    assert evidence.status is EvidenceStatus.PRESERVED


def test_evidence_preserves_aggregate_identity_after_lifecycle_transition() -> None:
    evidence = create_evidence()
    evidence_id = evidence.evidence_id

    evidence.preserve()
    evidence.process()
    evidence.analyze()

    assert evidence.evidence_id == evidence_id
    assert hash(evidence) == hash(evidence_id)
