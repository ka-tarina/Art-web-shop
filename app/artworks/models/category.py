"""Module for representing category in the system"""
from uuid import uuid4
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.db.database import Base


class Category(Base):
    """A class representing a category in the system."""
    __tablename__ = "category"
    id = Column(String(50), primary_key=True, default=uuid4, index=True)
    name = Column(String(100), unique=True, index=True)
    artworks = relationship("Artwork", back_populates="category")

    def __init__(self, name: str):
        self.name = name
