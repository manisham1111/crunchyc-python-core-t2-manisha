
class OrganizerError(Exception):
    """Base exception for organizer errors."""


class SourceFolderError(OrganizerError):
    """Raised when source folder is invalid."""


class ConfigError(OrganizerError):
    """Raised when configuration is invalid."""


class FileOperationError(OrganizerError):
    """Raised when a file operation fails."""
