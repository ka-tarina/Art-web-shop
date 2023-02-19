from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import sqltypes
from sqlalchemy.testing.schema import Column

from app.users.models import User, UserRole


class Admin(User):
    """A class representig an admin in the system."""
    __tablename__ = "admins"
    id = Column(String(50), ForeignKey("users.id"), primary_key=True)
    role = Column(sqltypes.Enum(UserRole), default=UserRole.ADMIN)
