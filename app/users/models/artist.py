from uuid import uuid4
from sqlalchemy import Column, ForeignKey, ForeignKeyConstraint, String
from sqlalchemy.orm import relationship
from app.db.database import Base


class Artist(Base):
    """A class representing an artist in the system."""
    __tablename__ = "artists"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    user_id = Column(String(50), ForeignKey("users.id"), unique=True)
    status = Column(String(50), default="pending")

    user = relationship("User", back_populates="artist")

    def __init__(self, user_id, status="pending"):
        """Initializes a new Artist object."""
        self.user_id = user_id
        self.status = status
