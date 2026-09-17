"""Value object representing the identity of an investigation case."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class InvestigationCaseId:
    """Immutable identifier for an investigation case."""

    value: str

    def __post_init__(self) -> None:
        if not self.value.strip():
            raise ValueError("InvestigationCaseId value cannot be empty.")
