"""Identity of a chain of custody."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ChainOfCustodyId:
    """Immutable identifier for a chain of custody."""

    value: str

    def __post_init__(self) -> None:
        if not self.value.strip():
            raise ValueError("ChainOfCustodyId value cannot be empty.")
