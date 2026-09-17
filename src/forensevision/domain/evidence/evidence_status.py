"""Lifecycle statuses for digital evidence."""

from enum import StrEnum


class EvidenceStatus(StrEnum):
    """Lifecycle status of digital evidence."""

    REGISTERED = "registered"
    PRESERVED = "preserved"
    PROCESSED = "processed"
    ANALYZED = "analyzed"
    ARCHIVED = "archived"
