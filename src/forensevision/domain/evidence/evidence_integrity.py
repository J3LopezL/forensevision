"""Integrity information associated with digital evidence."""

from dataclasses import dataclass
from enum import StrEnum


class HashAlgorithm(StrEnum):
    """Supported cryptographic hash algorithms."""

    SHA256 = "sha256"
    SHA512 = "sha512"


@dataclass(frozen=True, slots=True)
class EvidenceIntegrity:
    """Immutable cryptographic integrity information for digital evidence."""

    algorithm: HashAlgorithm
    value: str

    def __post_init__(self) -> None:
        normalized_value = self.value.strip().lower()

        if not normalized_value:
            raise ValueError("EvidenceIntegrity value cannot be empty.")

        expected_length = {
            HashAlgorithm.SHA256: 64,
            HashAlgorithm.SHA512: 128,
        }[self.algorithm]

        if len(normalized_value) != expected_length:
            raise ValueError(
                f"EvidenceIntegrity value must contain {expected_length} "
                f"hexadecimal characters for {self.algorithm.value}."
            )

        if any(character not in "0123456789abcdef" for character in normalized_value):
            raise ValueError(
                "EvidenceIntegrity value must contain only hexadecimal characters."
            )

        object.__setattr__(self, "value", normalized_value)
