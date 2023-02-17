from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.users.models import User, UserRole


class SuperUser(User):
    """A class representing a superuser in the system."""
    __tablename__ = "superusers"
    id = Column(String(50), ForeignKey("users.id"), primary_key=True)
    # Additional attributes for superusers
    access_level = Column(Integer, nullable=False)

    def __init__(self, name, email, password, status, access_level):
        """Initializes a new SuperUser object."""
        super().__init__(username=name, email=email, password=password, role=UserRole.SUPERUSER, status=status)
        self.access_level = access_level
