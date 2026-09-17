"""Source information associated with digital evidence."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EvidenceSource:
    """Immutable information describing the origin of digital evidence."""

    source: str

    def __post_init__(self) -> None:
        if not self.source.strip():
            raise ValueError("EvidenceSource source cannot be empty.")
