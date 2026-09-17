"""Tests for the EvidenceIntegrity value object."""

import pytest

from forensevision.domain.evidence.evidence_integrity import (
    EvidenceIntegrity,
    HashAlgorithm,
)


def test_evidence_integrity_accepts_sha256() -> None:
    value = "a" * 64

    integrity = EvidenceIntegrity(
        algorithm=HashAlgorithm.SHA256,
        value=value,
    )

    assert integrity.algorithm is HashAlgorithm.SHA256
    assert integrity.value == value


def test_evidence_integrity_accepts_sha512() -> None:
    value = "b" * 128

    integrity = EvidenceIntegrity(
        algorithm=HashAlgorithm.SHA512,
        value=value,
    )

    assert integrity.algorithm is HashAlgorithm.SHA512
    assert integrity.value == value


def test_evidence_integrity_normalizes_value_to_lowercase() -> None:
    value = "A" * 64

    integrity = EvidenceIntegrity(
        algorithm=HashAlgorithm.SHA256,
        value=value,
    )

    assert integrity.value == "a" * 64


def test_evidence_integrity_rejects_empty_value() -> None:
    with pytest.raises(ValueError, match="value cannot be empty"):
        EvidenceIntegrity(
            algorithm=HashAlgorithm.SHA256,
            value="",
        )


def test_evidence_integrity_rejects_invalid_sha256_length() -> None:
    with pytest.raises(ValueError, match="64 hexadecimal characters"):
        EvidenceIntegrity(
            algorithm=HashAlgorithm.SHA256,
            value="a" * 63,
        )


def test_evidence_integrity_rejects_invalid_sha512_length() -> None:
    with pytest.raises(ValueError, match="128 hexadecimal characters"):
        EvidenceIntegrity(
            algorithm=HashAlgorithm.SHA512,
            value="b" * 127,
        )


def test_evidence_integrity_rejects_non_hexadecimal_value() -> None:
    value = "g" * 64

    with pytest.raises(ValueError, match="only hexadecimal characters"):
        EvidenceIntegrity(
            algorithm=HashAlgorithm.SHA256,
            value=value,
        )


def test_evidence_integrity_is_immutable() -> None:
    integrity = EvidenceIntegrity(
        algorithm=HashAlgorithm.SHA256,
        value="a" * 64,
    )

    with pytest.raises(AttributeError):
        integrity.value = "b" * 64  # type: ignore[misc]
