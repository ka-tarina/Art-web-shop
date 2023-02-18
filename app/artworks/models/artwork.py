from uuid import uuid4
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, Enum
from sqlalchemy.orm import relationship
from app.db.database import Base


class Artwork(Base):
    __tablename__ = "artwork"
    id = Column(String(36), primary_key=True, default=uuid4, unique=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String(500))
    price = Column(Float, index=True)
    image = Column(String(200))
    stock = Column(Integer)

    category_id = Column(Integer, ForeignKey("category.id"))
    category = relationship("Category", back_populates="artworks")

    status = Column(Boolean, default=True)

    artist_id = Column(Integer, ForeignKey("artist.id"))
    artist = relationship("Artist", back_populates="artworks")

    currency = Column(Enum("RSD", "EUR", name="currency_type"), default="RSD", server_default="RSD")

    def __init__(self, name: str, description: str, price: float, image: str, stock: int, category_id: int,
                 status: bool, artist_id: int, currency: str):
        self.name = name
        self.description = description
        self.price = price
        self.image = image
        self.stock = stock
        self.category_id = category_id
        self.status = status
        self.artist_id = artist_id
        self.currency = currency
