"""Tests for the EvidenceMetadata value object."""

import pytest

from forensevision.domain.evidence.evidence_metadata import EvidenceMetadata


def test_evidence_metadata_accepts_valid_values() -> None:
    metadata = EvidenceMetadata(
        filename="evidence.jpg",
        mime_type="image/jpeg",
        size_bytes=1024,
    )

    assert metadata.filename == "evidence.jpg"
    assert metadata.mime_type == "image/jpeg"
    assert metadata.size_bytes == 1024


def test_evidence_metadata_accepts_zero_size() -> None:
    metadata = EvidenceMetadata(
        filename="empty.txt",
        mime_type="text/plain",
        size_bytes=0,
    )

    assert metadata.size_bytes == 0


def test_evidence_metadata_rejects_empty_filename() -> None:
    with pytest.raises(ValueError, match="filename cannot be empty"):
        EvidenceMetadata(
            filename="",
            mime_type="image/jpeg",
            size_bytes=1024,
        )


def test_evidence_metadata_rejects_whitespace_filename() -> None:
    with pytest.raises(ValueError, match="filename cannot be empty"):
        EvidenceMetadata(
            filename="   ",
            mime_type="image/jpeg",
            size_bytes=1024,
        )


def test_evidence_metadata_rejects_empty_mime_type() -> None:
    with pytest.raises(ValueError, match="mime_type cannot be empty"):
        EvidenceMetadata(
            filename="evidence.jpg",
            mime_type="",
            size_bytes=1024,
        )


def test_evidence_metadata_rejects_negative_size() -> None:
    with pytest.raises(ValueError, match="size_bytes cannot be negative"):
        EvidenceMetadata(
            filename="evidence.jpg",
            mime_type="image/jpeg",
            size_bytes=-1,
        )


def test_evidence_metadata_is_immutable() -> None:
    metadata = EvidenceMetadata(
        filename="evidence.jpg",
        mime_type="image/jpeg",
        size_bytes=1024,
    )

    with pytest.raises(AttributeError):
        metadata.filename = "other.jpg"  # type: ignore[misc]
