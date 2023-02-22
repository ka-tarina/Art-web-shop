"""Module for order exception classes"""


class OrderExceptionCode(Exception):
    """Exception raised for errors related to order codes."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class OrderNotFoundException(Exception):
    """Exception raised when an order is not found."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class InvalidOrderStatusError(Exception):
    """Exception raised when an order has an invalid status."""
    def __init__(self, message, code):
        self.message = message
        self.code = code
