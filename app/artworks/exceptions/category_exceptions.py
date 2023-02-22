"""Module for category exception classes"""


class CategoryExceptionCode(Exception):
    """Exception raised when a category-related error occurs.."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class CategoryNotFoundException(Exception):
    """Exception raised when a category cannot be found."""
    def __init__(self, message, code):
        self.message = message
        self.code = code
