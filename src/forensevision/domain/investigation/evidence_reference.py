"""Reference to digital evidence from an investigation case."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EvidenceReference:
    """Immutable reference to an evidence aggregate."""

    evidence_id: str

    def __post_init__(self) -> None:
        if not self.evidence_id.strip():
            raise ValueError("EvidenceReference evidence_id cannot be empty.")
