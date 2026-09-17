"""Metadata associated with digital evidence."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EvidenceMetadata:
    """Immutable technical metadata associated with digital evidence."""

    filename: str
    mime_type: str
    size_bytes: int

    def __post_init__(self) -> None:
        if not self.filename.strip():
            raise ValueError("EvidenceMetadata filename cannot be empty.")

        if not self.mime_type.strip():
            raise ValueError("EvidenceMetadata mime_type cannot be empty.")

        if self.size_bytes < 0:
            raise ValueError("EvidenceMetadata size_bytes cannot be negative.")
