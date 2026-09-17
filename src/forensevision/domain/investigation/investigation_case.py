"""Aggregate root representing a forensic investigation case."""

from forensevision.domain.investigation.evidence_reference import (
    EvidenceReference,
)
from forensevision.domain.investigation.investigation_case_id import (
    InvestigationCaseId,
)
from forensevision.domain.investigation.investigation_case_status import (
    InvestigationCaseStatus,
)


class InvestigationCase:
    """Aggregate root for a forensic investigation case."""

    __slots__ = (
        "_case_id",
        "_nunc",
        "_status",
        "_evidence_references",
    )

    def __init__(
        self,
        case_id: InvestigationCaseId,
        nunc: str,
    ) -> None:
        if not nunc.strip():
            raise ValueError("InvestigationCase nunc cannot be empty.")

        self._case_id = case_id
        self._nunc = nunc
        self._status = InvestigationCaseStatus.OPEN
        self._evidence_references: set[EvidenceReference] = set()

    @property
    def case_id(self) -> InvestigationCaseId:
        """Return the investigation case identity."""
        return self._case_id

    @property
    def nunc(self) -> str:
        """Return the external criminal case identifier."""
        return self._nunc

    @property
    def status(self) -> InvestigationCaseStatus:
        """Return the current investigation case status."""
        return self._status

    @property
    def evidence_references(self) -> frozenset[EvidenceReference]:
        """Return the evidence references associated with the case."""
        return frozenset(self._evidence_references)

    def add_evidence_reference(
        self,
        evidence_reference: EvidenceReference,
    ) -> None:
        """Associate an evidence reference with the investigation case."""
        self._evidence_references.add(evidence_reference)

    def remove_evidence_reference(
        self,
        evidence_reference: EvidenceReference,
    ) -> None:
        """Remove an evidence reference from the investigation case."""
        self._evidence_references.discard(evidence_reference)

    def __eq__(self, other: object) -> bool:
        """Compare investigation cases by identity."""
        if not isinstance(other, InvestigationCase):
            return NotImplemented

        return self.case_id == other.case_id

    def __hash__(self) -> int:
        """Return a hash based on the investigation case identity."""
        return hash(self.case_id)
