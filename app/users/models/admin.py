from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.testing.schema import Column

from app.users.models import User, UserRole


class Admin(User):
    """A class representig an admin in the system."""
    __tablename__ = "admins"
    id = Column(String(50), ForeignKey("users.id"), primary_key=True)

    def __init__(self, username, email, password, status):
        """Initializes a new Admin object."""
        super().__init__(username=username, email=email, password=password, role=UserRole.ADMIN, status=status)