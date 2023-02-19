from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.orders.models import Order


class CartItem(Base):
    __tablename__ = "cart_item"
    id = Column(String(50), primary_key=True, index=True)

    cart_id = Column(String(50), ForeignKey("cart.id"), index=True)

    artwork_id = Column(String(50), ForeignKey("artwork.id"), index=True)
    artwork = relationship("Artwork", back_populates="carts")

    quantity = Column(Integer, default=1)

    @property
    def price(self):
        return self.artwork.price * self.quantity

    @property
    def name(self):
        return self.artwork.name

    @property
    def image(self):
        return self.artwork.image

    @property
    def description(self):
        return self.artwork.description

    @property
    def stock(self):
        return self.artwork.stock

    @property
    def category_id(self):
        return self.artwork.category_id

    @property
    def artist_id(self):
        return self.artwork.artist_id

    @property
    def currency(self):
        return self.artwork.currency

    def __init__(self, cart_id: str, artwork_id: str, quantity: int):
        self.cart_id = cart_id
        self.artwork_id = artwork_id
        self.quantity = quantity
