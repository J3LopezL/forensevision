"""Actor responsible for a chain-of-custody action."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CustodyActor:
    """Immutable identity of the actor responsible for a custody action."""

    actor_id: str
    name: str

    def __post_init__(self) -> None:
        if not self.actor_id.strip():
            raise ValueError("CustodyActor actor_id cannot be empty.")

        if not self.name.strip():
            raise ValueError("CustodyActor name cannot be empty.")
