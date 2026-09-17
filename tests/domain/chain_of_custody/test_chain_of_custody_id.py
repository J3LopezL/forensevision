"""Tests for the ChainOfCustodyId value object."""

import pytest

from forensevision.domain.chain_of_custody.chain_of_custody_id import (
    ChainOfCustodyId,
)


def test_chain_of_custody_id_accepts_non_empty_value() -> None:
    chain_id = ChainOfCustodyId("CHAIN-000001")

    assert chain_id.value == "CHAIN-000001"


def test_chain_of_custody_id_rejects_empty_value() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        ChainOfCustodyId("")


def test_chain_of_custody_id_rejects_whitespace_only_value() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        ChainOfCustodyId("   ")


def test_chain_of_custody_id_is_immutable() -> None:
    chain_id = ChainOfCustodyId("CHAIN-000001")

    with pytest.raises(AttributeError):
        chain_id.value = "CHAIN-000002"  # type: ignore[misc]
