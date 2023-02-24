"""Module for User Exceptions"""


class UserInvalidPassword(Exception):
    """Exception raised when a user enters an invalid password."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserNotSuperUser(Exception):
    """Exception raised when a user tries to access resources
    or perform actions that are reserved for superusers."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserNotAdmin(Exception):
    """Exception raised when a user tries to access resources
    or perform actions that are reserved for admins."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserNotFoundError(Exception):
    """Exception raised when a user is not found in the system."""
    def __init__(self, message, code):
        self.message = message
        self.code = code
