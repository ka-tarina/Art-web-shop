"""Module for representing order in the system"""
from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import sqltypes
from app.db.database import Base
from app.orders.models.order_enum import OrderStatus


class Order(Base):
    """A class representing an order in the system."""
    __tablename__ = 'orders'
    id = Column(String(50), primary_key=True, default=uuid4, unique=True, index=True)

    user_id = Column(String(50), ForeignKey('users.id'), index=True)
    user = relationship("User", back_populates="orders", viewonly=True)

    customer = relationship("Customer",
                            back_populates="orders",
                            foreign_keys=[user_id],
                            overlaps="orders",
                            viewonly=True)

    order_date = Column(DateTime, default=datetime.utcnow, index=True)
    total_price = Column(Float, index=True)

    shipping_address = Column(String(500), index=True)
    order_status = Column(sqltypes.Enum(OrderStatus), default=OrderStatus.PENDING, index=True)

    artwork_id = Column(String(50), ForeignKey("artworks.id"), index=True)
    artwork = relationship("Artwork", back_populates="orders")

    def __init__(self,
                 user_id: str,
                 total_price: float,
                 shipping_address: str,
                 artwork_id: str):
        self.user_id = user_id
        self.order_date = datetime.now()
        self.total_price = total_price
        self.shipping_address = shipping_address
        self.artwork_id = artwork_id
        self.order_status = OrderStatus.PENDING
