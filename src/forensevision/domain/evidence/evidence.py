"""Aggregate root representing digital evidence."""

from __future__ import annotations

from typing import Any

from forensevision.domain.evidence.evidence_id import EvidenceId
from forensevision.domain.evidence.evidence_integrity import EvidenceIntegrity
from forensevision.domain.evidence.evidence_metadata import EvidenceMetadata
from forensevision.domain.evidence.evidence_source import EvidenceSource
from forensevision.domain.evidence.evidence_type import EvidenceType


class Evidence:
    """Aggregate root representing a piece of digital evidence."""

    __slots__ = (
        "_evidence_id",
        "_evidence_type",
        "_metadata",
        "_source",
        "_integrity",
    )

    def __init__(
        self,
        evidence_id: EvidenceId,
        evidence_type: EvidenceType,
        metadata: EvidenceMetadata,
        source: EvidenceSource,
        integrity: EvidenceIntegrity,
    ) -> None:
        self._evidence_id = evidence_id
        self._evidence_type = evidence_type
        self._metadata = metadata
        self._source = source
        self._integrity = integrity

    @property
    def evidence_id(self) -> EvidenceId:
        """Return the unique identity of the evidence."""
        return self._evidence_id

    @property
    def evidence_type(self) -> EvidenceType:
        """Return the technical type of the evidence."""
        return self._evidence_type

    @property
    def metadata(self) -> EvidenceMetadata:
        """Return the technical metadata of the evidence."""
        return self._metadata

    @property
    def source(self) -> EvidenceSource:
        """Return the origin of the evidence."""
        return self._source

    @property
    def integrity(self) -> EvidenceIntegrity:
        """Return the cryptographic integrity information."""
        return self._integrity

    def __eq__(self, other: Any) -> bool:
        """Compare evidence entities by their identity."""
        if not isinstance(other, Evidence):
            return NotImplemented

        return self.evidence_id == other.evidence_id

    def __hash__(self) -> int:
        """Return a hash based on the evidence identity."""
        return hash(self.evidence_id)
