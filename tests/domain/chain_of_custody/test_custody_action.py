"""Tests for custody actions."""

from forensevision.domain.chain_of_custody.custody_action import CustodyAction


def test_custody_action_contains_expected_values() -> None:
    assert CustodyAction.COLLECTION.value == "collection"
    assert CustodyAction.TRANSFER.value == "transfer"
    assert CustodyAction.RECEIPT.value == "receipt"
    assert CustodyAction.PRESERVATION.value == "preservation"
    assert CustodyAction.ANALYSIS.value == "analysis"
    assert CustodyAction.RETURN.value == "return"
    assert CustodyAction.STORAGE.value == "storage"


def test_custody_action_is_string_compatible() -> None:
    assert CustodyAction.COLLECTION == "collection"


def test_custody_action_members_are_distinct() -> None:
    actions = list(CustodyAction)

    assert len(actions) == len(set(actions))
