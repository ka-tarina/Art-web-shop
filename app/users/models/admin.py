from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import sqltypes
from app.users.models import User
from app.users.enums import UserRole


class Admin(User):
    """A class representing an admin in the system."""
    __tablename__ = "admins"
    id = Column(String(50), ForeignKey("users.id"), primary_key=True)
    admin_role = Column(sqltypes.Enum(UserRole, native_enum=False), default=UserRole.ADMIN)

    user = relationship("User", back_populates="admin")
