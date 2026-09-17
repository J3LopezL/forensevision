"""Actions that can occur during the custody of digital evidence."""

from enum import StrEnum


class CustodyAction(StrEnum):
    """Supported actions in the chain of custody."""

    COLLECTION = "collection"
    TRANSFER = "transfer"
    RECEIPT = "receipt"
    PRESERVATION = "preservation"
    ANALYSIS = "analysis"
    RETURN = "return"
    STORAGE = "storage"
