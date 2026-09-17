"""Lifecycle statuses for investigation cases."""

from enum import StrEnum


class InvestigationCaseStatus(StrEnum):
    """Lifecycle status of an investigation case."""

    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"
    ARCHIVED = "archived"
