"""Module for representing Artist in the system"""
from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import relationship
from app.users.models import User
from app.users.enums import UserRole, UserStatus

followers = Table(
    "followers",
    User.metadata,
    Column("artist_id", String(50), ForeignKey("users.id")),
    Column("customer_id", String(50), ForeignKey("users.id")),
)


class Artist(User):
    """A class representing an artist in the system."""
    __tablename__ = "artists"
    id = Column(String(50), ForeignKey("users.id"), primary_key=True)

    # Additional attributes for artists
    bio = Column(String(500), nullable=True)
    website = Column(String(100), nullable=True)

    # Relationships with other tables
    artworks = relationship("Artwork", back_populates="artist")
    user = relationship("User", back_populates="artist")

    followers = relationship(
        "Customer",
        secondary=followers,
        primaryjoin=(id == followers.c.artist_id),
        secondaryjoin=(id == followers.c.customer_id),
        back_populates="follows",
        foreign_keys=[followers.c.artist_id, followers.c.customer_id]
    )

    __mapper_args__ = {
        'polymorphic_identity': UserRole.ARTIST
    }

    def __init__(self, username, email, password, bio="", website=""):
        """Initializes a new Artist object."""
        super().__init__(
            username=username,
            email=email,
            password=password,
            status=UserStatus.ACTIVE,
            role=UserRole.ARTIST
        )
        self.bio = bio
        self.website = website
