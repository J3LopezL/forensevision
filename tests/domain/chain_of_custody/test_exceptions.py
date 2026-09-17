"""Tests for chain-of-custody domain exceptions."""

from forensevision.domain.chain_of_custody.exceptions import (
    CustodyEventChronologyError,
    CustodyEvidenceMismatchError,
)


def test_custody_evidence_mismatch_error_is_value_error() -> None:
    error = CustodyEvidenceMismatchError("Evidence mismatch.")

    assert isinstance(error, ValueError)


def test_custody_event_chronology_error_is_value_error() -> None:
    error = CustodyEventChronologyError("Invalid chronology.")

    assert isinstance(error, ValueError)
