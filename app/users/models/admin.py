from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import sqltypes

from app.users.enums import UserRole, UserStatus
from app.users.models import User


class Admin(User):
    """A class representing an admin in the system."""

    __tablename__ = "admins"
    id = Column(String(50), ForeignKey("users.id"), primary_key=True)
    role = Column(sqltypes.Enum(UserRole, native_enum=False), default=UserRole.ADMIN)

    user = relationship("User", back_populates="admin")

    def __init__(self, username, email, password):
        """Initializes a new Admin object."""
        super().__init__(
            username=username,
            email=email,
            password=password,
            status=UserStatus.ACTIVE,
            role=UserRole.ADMIN,
        )
