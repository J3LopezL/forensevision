"""Identity of a chain-of-custody event."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CustodyEventId:
    """Immutable identifier for a custody event."""

    value: str

    def __post_init__(self) -> None:
        if not self.value.strip():
            raise ValueError("CustodyEventId value cannot be empty.")
