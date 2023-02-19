from uuid import uuid4
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import sqltypes
from app.db.database import Base
from app.orders.models.order_enum import OrderStatus


class Order(Base):
    """A class representing an order in the system."""
    __tablename__ = 'orders'
    id = Column(String(50), primary_key=True, default=uuid4, unique=True, index=True)
    user_id = Column(String(50), ForeignKey('users.id'))
    order_date = Column(DateTime)
    total_price = Column(Float, index=True)
    shipping_address = Column(String(200), index=True)
    order_status = Column(sqltypes.Enum(OrderStatus), index=True)

    # Define a relationship to the User model
    user = relationship('User', back_populates='orders')

    def __init__(self, user_id: int, total_price: float, shipping_address: str):
        """Initializes a new Order object."""
        self.user_id = user_id
        self.total_price = total_price
        self.shipping_address = shipping_address
