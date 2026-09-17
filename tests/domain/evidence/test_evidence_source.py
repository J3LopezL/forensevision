"""Tests for the EvidenceSource value object."""

import pytest

from forensevision.domain.evidence.evidence_source import EvidenceSource


def test_evidence_source_accepts_non_empty_value() -> None:
    source = EvidenceSource("mobile_device")

    assert source.source == "mobile_device"


def test_evidence_source_rejects_empty_value() -> None:
    with pytest.raises(ValueError, match="source cannot be empty"):
        EvidenceSource("")


def test_evidence_source_rejects_whitespace_only_value() -> None:
    with pytest.raises(ValueError, match="source cannot be empty"):
        EvidenceSource("   ")


def test_evidence_source_equality_is_based_on_value() -> None:
    first = EvidenceSource("mobile_device")
    second = EvidenceSource("mobile_device")

    assert first == second


def test_evidence_source_is_immutable() -> None:
    source = EvidenceSource("mobile_device")

    with pytest.raises(AttributeError):
        source.source = "cloud"  # type: ignore[misc]
