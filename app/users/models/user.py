from uuid import uuid4
from sqlalchemy import Boolean, Column, String
from app.db.database import Base


class User(Base):
    """A class representing a user in the system."""
    __tablename__ = "users"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(100))
    is_active = Column(Boolean)
    is_superuser = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    is_artist = Column(Boolean, default=False)

    def __init__(self, name, email, password, is_active=True, is_superuser=False, is_admin=False, is_artist=False):
        """Initializes a new User object."""
        self.name = name
        self.email = email
        self.password = password
        self.is_active = is_active
        self.is_superuser = is_superuser
        self.is_admin = is_admin
        self.is_artist = is_artist
