"""Module defines two enumeration classes: UserRole and UserStatus."""
from enum import Enum


class UserRole(str, Enum):
    """Defines the different roles that a user can have in the system."""
    SUPERUSER = "superuser"
    ADMIN = "admin"
    ARTIST = "artist"
    CUSTOMER = "customer"


class UserStatus(str, Enum):
    """Defines the different status that a user account can have."""
    ACTIVE = "active"
    PENDING = "pending"
    INACTIVE = "inactive"
