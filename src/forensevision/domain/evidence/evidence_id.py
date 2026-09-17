"""Value object representing the identity of digital evidence."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EvidenceId:
    """Immutable identifier for a piece of digital evidence."""

    value: str

    def __post_init__(self) -> None:
        if not self.value.strip():
            raise ValueError("EvidenceId value cannot be empty.")
