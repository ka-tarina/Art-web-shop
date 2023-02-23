"""Module for representing artwork in the system"""
from uuid import uuid4
from sqlalchemy import Column, String, Boolean, ForeignKey, Float, Enum
from sqlalchemy.orm import relationship
from app.db.database import Base


class Artwork(Base):
    """A class representing an artwork in the system."""
    __tablename__ = "artworks"
    id = Column(String(50), primary_key=True, default=uuid4, unique=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String(500))
    price = Column(Float, index=True)
    image = Column(String(200))
    stock = int
    category_id = Column(String(50), ForeignKey("category.id"))
    status = Column(Boolean, default=True)
    artist_id = Column(String(50), ForeignKey("users.id"))
    currency = Column(Enum("RSD", "EUR", name="currency_type"), default="RSD", server_default="RSD")

    category = relationship("Category", back_populates="artworks")
    artist = relationship("Artist", back_populates="artworks", overlaps="artwork_artist")

    artwork_artist = relationship("Artist", back_populates="artworks", foreign_keys=[artist_id])

    orders = relationship("Order", uselist=False, back_populates="artwork")

    def __init__(self,
                 name: str,
                 description: str,
                 price: float,
                 image: str,
                 stock: int,
                 category_id: int,
                 artist_id: int):
        self.name = name
        self.description = description
        self.price = price
        self.image = image
        self.stock = stock
        self.category_id = category_id
        self.status = True
        self.artist_id = artist_id
        self.currency = "RSD"
