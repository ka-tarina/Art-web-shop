from enum import Enum
from uuid import uuid4
from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship
from app.db.database import Base


class UserRole(str, Enum):
    SUPERUSER = "superuser"
    ADMIN = "admin"
    ARTIST = "artist"
    CUSTOMER = "customer"


class UserStatus(str, Enum):
    ACTIVE = "active"
    PENDING = "pending"
    INACTIVE = "inactive"


class User(Base):
    """A class representing a user in the system."""
    __tablename__ = "users"
    id = Column(String(50), primary_key=True, default=uuid4, index=True, autoincrement=False)
    username = Column(String(100), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(100), nullable=False)
    status = Column(Enum(UserStatus), nullable=False)
    role = Column(Enum(UserRole), nullable=False)

    # Relationships with other tables
    artwork = relationship("Artwork", back_populates="user")
    orders = relationship("Order", back_populates="user")

    def __init__(self, name, email, password, role, status):
        """Initializes a new User object."""
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.status = status
