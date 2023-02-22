"""Module for artwork exception classes"""


class ArtworkExceptionCode(Exception):
    """Exception raised when an artwork-related error occurs.."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class ArtworkNotFoundException(Exception):
    """Exception raised when an artwork cannot be found."""
    def __init__(self, message, code):
        self.message = message
        self.code = code
