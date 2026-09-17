"""Tests for the digital evidence lifecycle policy."""

import pytest

from forensevision.domain.evidence.evidence_lifecycle import EvidenceLifecycle
from forensevision.domain.evidence.evidence_status import EvidenceStatus


@pytest.mark.parametrize(
    ("current_status", "expected_status"),
    [
        (EvidenceStatus.REGISTERED, EvidenceStatus.PRESERVED),
        (EvidenceStatus.PRESERVED, EvidenceStatus.PROCESSED),
        (EvidenceStatus.PROCESSED, EvidenceStatus.ANALYZED),
        (EvidenceStatus.ANALYZED, EvidenceStatus.ARCHIVED),
    ],
)
def test_next_status_returns_valid_transition(
    current_status: EvidenceStatus,
    expected_status: EvidenceStatus,
) -> None:
    assert EvidenceLifecycle.next_status(current_status) is expected_status


def test_next_status_returns_none_for_archived_evidence() -> None:
    assert EvidenceLifecycle.next_status(EvidenceStatus.ARCHIVED) is None


@pytest.mark.parametrize(
    ("current_status", "requested_status"),
    [
        (EvidenceStatus.REGISTERED, EvidenceStatus.PRESERVED),
        (EvidenceStatus.PRESERVED, EvidenceStatus.PROCESSED),
        (EvidenceStatus.PROCESSED, EvidenceStatus.ANALYZED),
        (EvidenceStatus.ANALYZED, EvidenceStatus.ARCHIVED),
    ],
)
def test_is_valid_transition_accepts_valid_transitions(
    current_status: EvidenceStatus,
    requested_status: EvidenceStatus,
) -> None:
    assert EvidenceLifecycle.is_valid_transition(
        current_status,
        requested_status,
    )


@pytest.mark.parametrize(
    ("current_status", "requested_status"),
    [
        (EvidenceStatus.REGISTERED, EvidenceStatus.PROCESSED),
        (EvidenceStatus.REGISTERED, EvidenceStatus.ANALYZED),
        (EvidenceStatus.REGISTERED, EvidenceStatus.ARCHIVED),
        (EvidenceStatus.PRESERVED, EvidenceStatus.REGISTERED),
        (EvidenceStatus.PROCESSED, EvidenceStatus.PRESERVED),
        (EvidenceStatus.ANALYZED, EvidenceStatus.PROCESSED),
        (EvidenceStatus.ARCHIVED, EvidenceStatus.ANALYZED),
    ],
)
def test_is_valid_transition_rejects_invalid_transitions(
    current_status: EvidenceStatus,
    requested_status: EvidenceStatus,
) -> None:
    assert not EvidenceLifecycle.is_valid_transition(
        current_status,
        requested_status,
    )
