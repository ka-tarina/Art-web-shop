from uuid import uuid4
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class Cart(Base):
    __tablename__ = "cart"
    id = Column(String(50), primary_key=True, default=uuid4, unique=True, index=True)

    user_id = Column(String(50), ForeignKey("users.id"), index=True)
    user = relationship("User", back_populates="cart")

    total_price = Column(Float, default=0.0)

    items = relationship("CartItem", back_populates="cart")

    def __init__(self, user_id: str):
        self.user_id = user_id
        self.total_price = 0.0
