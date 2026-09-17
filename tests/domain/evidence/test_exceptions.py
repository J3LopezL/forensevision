"""Tests for digital evidence domain exceptions."""

import pytest

from forensevision.domain.evidence.evidence_status import EvidenceStatus
from forensevision.domain.evidence.exceptions import (
    InvalidEvidenceStatusTransitionError,
)


def test_invalid_evidence_status_transition_error_contains_statuses() -> None:
    error = InvalidEvidenceStatusTransitionError(
        current_status=EvidenceStatus.REGISTERED,
        requested_status=EvidenceStatus.ANALYZED,
    )

    assert error.current_status is EvidenceStatus.REGISTERED
    assert error.requested_status is EvidenceStatus.ANALYZED


def test_invalid_evidence_status_transition_error_has_descriptive_message() -> None:
    with pytest.raises(
        InvalidEvidenceStatusTransitionError,
        match="registered -> analyzed",
    ):
        raise InvalidEvidenceStatusTransitionError(
            current_status=EvidenceStatus.REGISTERED,
            requested_status=EvidenceStatus.ANALYZED,
        )
