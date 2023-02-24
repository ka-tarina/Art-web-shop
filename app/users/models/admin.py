"""Module for representing admin in the system"""
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.users.enums import UserRole, UserStatus
from app.users.models import User


class Admin(User):
    """A class representing an admin in the system."""

    __tablename__ = "admins"
    id = Column(String(50), ForeignKey("users.id"), primary_key=True)

    user = relationship("User", back_populates="admin")

    __mapper_args__ = {
        'polymorphic_identity': UserRole.ADMIN
    }

    def __init__(self, username, email, password):
        """Initializes a new Admin object."""
        super().__init__(
            username=username,
            email=email,
            password=password,
            status=UserStatus.ACTIVE,
            role=UserRole.ADMIN,
        )
