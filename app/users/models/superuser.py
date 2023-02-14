from sqlalchemy import Column, Integer
from user import User, UserRole


class SuperUser(User):
    """A class representing a superuser in the system."""
    __tablename__ = "superusers"

    # Additional attributes for superusers
    access_level = Column(Integer, nullable=False)

    def __init__(self, name, email, password, status, access_level):
        """Initializes a new SuperUser object."""
        super().__init__(name=name, email=email, password=password, role=UserRole.SUPERUSER, status=status)
        self.access_level = access_level
