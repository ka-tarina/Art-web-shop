from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Boolean, ForeignKey, Table
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

    # Additional attributes for customers
    id = Column(String(50), ForeignKey("users.id"), primary_key=True)
    is_verified = Column(Boolean, default=False, nullable=False)

    # Relationships with other tables
    orders = relationship("Order", back_populates="customer")
    collections = relationship("Collection", back_populates="customer")
    following = relationship("Artist", secondary=follows, back_populates="followers")

    def __init__(self, name, email, password, status):
        """Initializes a new Customer object."""
        super().__init__(username=name, email=email, password=password, role=UserRole.CUSTOMER, status=status)
