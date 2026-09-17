"""Individual event in the chain of custody of digital evidence."""

from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

from forensevision.domain.chain_of_custody.custody_action import (
    CustodyAction,
)
from forensevision.domain.chain_of_custody.custody_actor import CustodyActor
from forensevision.domain.chain_of_custody.custody_event_id import (
    CustodyEventId,
)


@dataclass(frozen=True, slots=True)
class CustodyEvent:
    """Immutable record of an action performed on digital evidence."""

    event_id: CustodyEventId
    evidence_id: str
    actor: CustodyActor
    action: CustodyAction
    occurred_at: datetime
    description: str

    def __post_init__(self) -> None:
        if not self.evidence_id.strip():
            raise ValueError("CustodyEvent evidence_id cannot be empty.")

        if not self.description.strip():
            raise ValueError("CustodyEvent description cannot be empty.")

        if self.occurred_at.tzinfo is None:
            raise ValueError(
                "CustodyEvent occurred_at must include a timezone."
            )

        if self.occurred_at.utcoffset() != timedelta(0):
            raise ValueError("CustodyEvent occurred_at must be in UTC.")

        object.__setattr__(self, "occurred_at", self.occurred_at.astimezone(UTC))
