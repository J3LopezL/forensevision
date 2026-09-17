"""Domain exceptions for digital evidence."""

from forensevision.domain.evidence.evidence_status import EvidenceStatus


class InvalidEvidenceStatusTransitionError(ValueError):
    """Raised when an evidence status transition is not allowed."""

    def __init__(
        self,
        current_status: EvidenceStatus,
        requested_status: EvidenceStatus,
    ) -> None:
        self.current_status = current_status
        self.requested_status = requested_status

        super().__init__(
            f"Invalid evidence status transition: "
            f"{current_status.value} -> {requested_status.value}."
        )
