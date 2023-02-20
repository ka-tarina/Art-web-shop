from uuid import uuid4
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, Enum
from sqlalchemy.orm import relationship
from app.db.database import Base


class Artwork(Base):
    __tablename__ = "artworks"
    id = Column(String(50), primary_key=True, default=uuid4, unique=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String(500))
    price = Column(Float, index=True)
    image = Column(String(200))

    category_id = Column(String(50), ForeignKey("category.id"))
    category = relationship("Category", back_populates="artworks")

    status = Column(Boolean, default=True)
    stock = int

    artist_id = Column(String(50), ForeignKey("artists.id"))
    artist = relationship("Artist", back_populates="artworks")

    currency = Column(Enum("RSD", "EUR", name="currency_type"), default="RSD", server_default="RSD")

    order = relationship("Order", uselist=False, back_populates="artworks")

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
