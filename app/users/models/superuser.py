from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.users.models import User, UserRole


class SuperUser(User):
    """A class representing a superuser in the system."""
    __tablename__ = "superusers"
    id = Column(String(50), ForeignKey("users.id"), primary_key=True)

    def __init__(self, name, email, password, role, status):
        """Initializes a new SuperUser object."""
        super().__init__(username=name, email=email, password=password, role=UserRole.SUPERUSER, status=status)
        self.role = role
