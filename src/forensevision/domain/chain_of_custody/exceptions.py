"""Domain exceptions for chain of custody."""


class CustodyEvidenceMismatchError(ValueError):
    """Raised when a custody event belongs to another evidence."""


class CustodyEventChronologyError(ValueError):
    """Raised when a custody event violates chronological order."""
