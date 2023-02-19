from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import sqltypes
from app.users.models import User, UserRole


class SuperUser(User):
    """A class representing a superuser in the system."""
    __tablename__ = "superusers"
    id = Column(String(50), ForeignKey("users.id"), primary_key=True)
    role = Column(sqltypes.Enum(UserRole), default=UserRole.SUPERUSER)
