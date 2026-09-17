"""Aggregate root representing the chain of custody of digital evidence."""

from datetime import datetime

from forensevision.domain.chain_of_custody.chain_of_custody_id import (
    ChainOfCustodyId,
)
from forensevision.domain.chain_of_custody.custody_event import CustodyEvent
from forensevision.domain.chain_of_custody.exceptions import (
    CustodyEventChronologyError,
    CustodyEvidenceMismatchError,
)


class ChainOfCustody:
    """Aggregate root for the custody history of a digital evidence item."""

    __slots__ = (
        "_chain_id",
        "_evidence_id",
        "_events",
    )

    def __init__(
        self,
        chain_id: ChainOfCustodyId,
        evidence_id: str,
    ) -> None:
        if not evidence_id.strip():
            raise ValueError("ChainOfCustody evidence_id cannot be empty.")

        self._chain_id = chain_id
        self._evidence_id = evidence_id
        self._events: list[CustodyEvent] = []

    @property
    def chain_id(self) -> ChainOfCustodyId:
        """Return the chain-of-custody identity."""
        return self._chain_id

    @property
    def evidence_id(self) -> str:
        """Return the evidence identity associated with the chain."""
        return self._evidence_id

    @property
    def events(self) -> tuple[CustodyEvent, ...]:
        """Return the custody events in chronological order."""
        return tuple(self._events)

    @property
    def last_event_at(self) -> datetime | None:
        """Return the timestamp of the most recent custody event."""
        if not self._events:
            return None

        return self._events[-1].occurred_at

    def add_event(self, event: CustodyEvent) -> None:
        """Add a valid event to the custody chain."""
        if event.evidence_id != self.evidence_id:
            raise CustodyEvidenceMismatchError(
                "Custody event evidence_id does not match the chain evidence_id."
            )

        if (
            self.last_event_at is not None
            and event.occurred_at < self.last_event_at
        ):
            raise CustodyEventChronologyError(
                "Custody event occurred_at cannot be earlier than "
                "the last custody event."
            )

        self._events.append(event)

    def __eq__(self, other: object) -> bool:
        """Compare custody chains by identity."""
        if not isinstance(other, ChainOfCustody):
            return NotImplemented

        return self.chain_id == other.chain_id

    def __hash__(self) -> int:
        """Return a hash based on the chain identity."""
        return hash(self.chain_id)
