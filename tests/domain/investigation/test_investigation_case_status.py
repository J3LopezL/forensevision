"""Tests for investigation case lifecycle statuses."""

from forensevision.domain.investigation.investigation_case_status import (
    InvestigationCaseStatus,
)


def test_investigation_case_status_contains_expected_values() -> None:
    assert InvestigationCaseStatus.OPEN.value == "open"
    assert InvestigationCaseStatus.IN_PROGRESS.value == "in_progress"
    assert InvestigationCaseStatus.CLOSED.value == "closed"
    assert InvestigationCaseStatus.ARCHIVED.value == "archived"


def test_investigation_case_status_is_string_compatible() -> None:
    assert InvestigationCaseStatus.OPEN == "open"


def test_investigation_case_status_members_are_distinct() -> None:
    statuses = list(InvestigationCaseStatus)

    assert len(statuses) == len(set(statuses))
