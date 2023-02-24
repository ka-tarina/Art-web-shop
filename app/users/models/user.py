"""Module for representing User in the system"""
from uuid import uuid4
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import sqltypes
from app.db.database import Base
from app.users.enums import UserStatus, UserRole


class User(Base):
    """A class representing a user in the system."""
    __tablename__ = "users"
    id = Column(String(50), primary_key=True, default=(uuid4()), index=True, autoincrement=False)
    username = Column(String(100), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(100), nullable=False)
    status = Column(sqltypes.Enum(UserStatus, native_enum=False), nullable=False)
    role = Column(sqltypes.Enum(UserRole, native_enum=False), nullable=False)

    # Relationships with other tables
    artwork = relationship("Artwork", back_populates="artist")
    orders = relationship("Order", back_populates="customer", overlaps="customer")

    superuser = relationship("SuperUser", uselist=False, back_populates="user")
    admin = relationship("Admin", uselist=False, back_populates="user")
    artist = relationship("Artist", uselist=False, back_populates="user")
    customer = relationship("Customer", uselist=False, back_populates="user")

    __mapper_args__ = {
        'polymorphic_on': role,
        'polymorphic_identity': UserRole.USER
    }

    def __init__(self, username, email, password, status, role):
        """Initializes a new User object."""
        self.username = username
        self.email = email
        self.password = password
        self.status = status
        self.role = role
