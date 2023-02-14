from uuid import uuid4
from sqlalchemy import Column, ForeignKey, ForeignKeyConstraint, String, Table
from sqlalchemy.orm import relationship
from user import User, UserRole


artist_followers = Table(
    "artist_followers",
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
    artwork = relationship("Artwork", back_populates="artist")

    followers = relationship(
        "Customer",
        secondary=artist_followers,
        back_populates="followed_artists"
    )

    def __init__(self, name, email, password, status, bio="", website=""):
        """Initializes a new Artist object."""
        super().__init__(name=name, email=email, password=password, role=UserRole.ARTIST, status=status)
        self.bio = bio
        self.website = website
