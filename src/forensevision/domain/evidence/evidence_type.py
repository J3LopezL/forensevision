"""Types of digital evidence handled by ForenseVisión."""

from enum import StrEnum


class EvidenceType(StrEnum):
    """Supported types of digital evidence."""

    FILE = "file"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    EMAIL = "email"
    NETWORK_CAPTURE = "network_capture"
    DATABASE = "database"
    LOG = "log"
    OTHER = "other"
