"""Tests for the InvestigationCase aggregate root."""

import pytest

from forensevision.domain.investigation.evidence_reference import (
    EvidenceReference,
)
from forensevision.domain.investigation.investigation_case import (
    InvestigationCase,
)
from forensevision.domain.investigation.investigation_case_id import (
    InvestigationCaseId,
)
from forensevision.domain.investigation.investigation_case_status import (
    InvestigationCaseStatus,
)


def create_case(
    case_id: str = "CASE-000001",
    nunc: str = "110016000000202600001",
) -> InvestigationCase:
    """Create a valid InvestigationCase instance for testing."""
    return InvestigationCase(
        case_id=InvestigationCaseId(case_id),
        nunc=nunc,
    )


def test_investigation_case_accepts_valid_components() -> None:
    case = create_case()

    assert case.case_id == InvestigationCaseId("CASE-000001")
    assert case.nunc == "110016000000202600001"
    assert case.status is InvestigationCaseStatus.OPEN


def test_investigation_case_identity_is_based_on_case_id() -> None:
    first = create_case("CASE-000001", "110016000000202600001")
    second = create_case("CASE-000001", "110016000000202600002")

    assert first == second


def test_investigation_cases_with_different_ids_are_not_equal() -> None:
    first = create_case("CASE-000001")
    second = create_case("CASE-000002")

    assert first != second


def test_investigation_case_identity_is_hashable() -> None:
    case = create_case()

    assert hash(case) == hash(InvestigationCaseId("CASE-000001"))


def test_investigation_case_id_is_read_only() -> None:
    case = create_case()

    with pytest.raises(AttributeError):
        case.case_id = InvestigationCaseId("CASE-000002")  # type: ignore[misc]


def test_investigation_case_nunc_is_read_only() -> None:
    case = create_case()

    with pytest.raises(AttributeError):
        case.nunc = "110016000000202600002"  # type: ignore[misc]


def test_investigation_case_status_is_read_only() -> None:
    case = create_case()

    with pytest.raises(AttributeError):
        case.status = InvestigationCaseStatus.CLOSED  # type: ignore[misc]


def test_investigation_case_rejects_empty_nunc() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        create_case(nunc="")


def test_investigation_case_rejects_whitespace_nunc() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        create_case(nunc="   ")


def test_investigation_case_starts_without_evidence_references() -> None:
    case = create_case()

    assert case.evidence_references == frozenset()


def test_investigation_case_can_add_evidence_reference() -> None:
    case = create_case()
    reference = EvidenceReference("EV-000001")

    case.add_evidence_reference(reference)

    assert reference in case.evidence_references


def test_investigation_case_can_remove_evidence_reference() -> None:
    case = create_case()
    reference = EvidenceReference("EV-000001")

    case.add_evidence_reference(reference)
    case.remove_evidence_reference(reference)

    assert reference not in case.evidence_references


def test_investigation_case_does_not_duplicate_evidence_references() -> None:
    case = create_case()
    first = EvidenceReference("EV-000001")
    second = EvidenceReference("EV-000001")

    case.add_evidence_reference(first)
    case.add_evidence_reference(second)

    assert len(case.evidence_references) == 1


def test_investigation_case_evidence_references_are_read_only() -> None:
    case = create_case()
    reference = EvidenceReference("EV-000001")

    case.add_evidence_reference(reference)

    references = case.evidence_references

    assert isinstance(references, frozenset)

    with pytest.raises(AttributeError):
        references.add(EvidenceReference("EV-000002"))  # type: ignore[attr-defined]


def test_investigation_case_identity_is_independent_of_evidence_references() -> None:
    first = create_case("CASE-000001")
    second = create_case("CASE-000001")

    first.add_evidence_reference(EvidenceReference("EV-000001"))

    assert first == second
