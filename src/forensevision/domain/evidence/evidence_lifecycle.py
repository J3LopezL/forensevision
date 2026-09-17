"""Lifecycle transition policy for digital evidence."""

from forensevision.domain.evidence.evidence_status import EvidenceStatus


class EvidenceLifecycle:
    """Domain policy defining valid evidence lifecycle transitions."""

    _TRANSITIONS: dict[EvidenceStatus, EvidenceStatus] = {
        EvidenceStatus.REGISTERED: EvidenceStatus.PRESERVED,
        EvidenceStatus.PRESERVED: EvidenceStatus.PROCESSED,
        EvidenceStatus.PROCESSED: EvidenceStatus.ANALYZED,
        EvidenceStatus.ANALYZED: EvidenceStatus.ARCHIVED,
    }

    @classmethod
    def next_status(
        cls,
        current_status: EvidenceStatus,
    ) -> EvidenceStatus | None:
        """Return the valid next status, if one exists."""
        return cls._TRANSITIONS.get(current_status)

    @classmethod
    def is_valid_transition(
        cls,
        current_status: EvidenceStatus,
        requested_status: EvidenceStatus,
    ) -> bool:
        """Return whether the requested transition is valid."""
        return cls.next_status(current_status) is requested_status

