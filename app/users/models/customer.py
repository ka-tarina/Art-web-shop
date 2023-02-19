from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Table
from app.db.database import Base
from app.users.models import User, UserRole


follows = Table(
    "follows",
    Base.metadata,
    Column("artist_id", String(50), ForeignKey("users.id")),
    Column("customer_id", String(50), ForeignKey("users.id")),
)


class Customer(User):
    """A class representing a customer in the system."""
    __tablename__ = "customers"
    id = Column(String(50), ForeignKey("users.id"), primary_key=True)

    # Relationships with other tables
    orders = relationship("Order", back_populates="customer")
    following = relationship("Artist", secondary=follows, back_populates="followers")
