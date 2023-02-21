from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Table
from app.db.database import Base
from app.users.models import User, Artist
from app.users.enums import UserRole, UserStatus

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
    user = relationship("User", back_populates="customer")
    orders = relationship("Order", back_populates="customer")

    follows = relationship(
        "Artist",
        secondary=follows,
        primaryjoin=(id == follows.c.customer_id),
        secondaryjoin=(id == follows.c.artist_id),
        back_populates="followers",
        foreign_keys=[follows.c.customer_id, follows.c.artist_id]
    )
    #
    # __mapper_args__ = {
    #     'polymorphic_identity': 'customer'
    # }

    def __init__(self, username, email, password):
        """Initializes a new Customer object."""
        super().__init__(
            username=username,
            email=email,
            password=password,
            status=UserStatus.ACTIVE,
            role=UserRole.CUSTOMER,
        )
