"""Tests for the InvestigationCaseId value object."""

import pytest

from forensevision.domain.investigation.investigation_case_id import (
    InvestigationCaseId,
)


def test_investigation_case_id_accepts_non_empty_value() -> None:
    case_id = InvestigationCaseId("CASE-000001")

    assert case_id.value == "CASE-000001"


def test_investigation_case_id_rejects_empty_value() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        InvestigationCaseId("")


def test_investigation_case_id_rejects_whitespace_only_value() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        InvestigationCaseId("   ")


def test_investigation_case_id_equality_is_based_on_value() -> None:
    first = InvestigationCaseId("CASE-000001")
    second = InvestigationCaseId("CASE-000001")

    assert first == second


def test_investigation_case_id_is_immutable() -> None:
    case_id = InvestigationCaseId("CASE-000001")

    with pytest.raises(AttributeError):
        case_id.value = "CASE-000002"  # type: ignore[misc]
