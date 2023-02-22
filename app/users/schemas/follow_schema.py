"""Module for following schemas."""
from pydantic import UUID4, BaseModel
from pydantic.schema import Optional, List
from app.users.schemas import ArtistSchema, CustomerSchema


class CustomerFollowedArtistSchema(BaseModel):
    """Schema representing Customer and Artist they follow."""
    customer_id: UUID4
    artist_id: UUID4
    username: str
    bio: Optional[str]

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class FollowSchema(BaseModel):
    """Schema for following or unfollowing artist by customer."""
    customer_id: UUID4
    artist_id: UUID4

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class FollowingArtistsSchema(BaseModel):
    """Schema for representing artist that Customer follows."""
    following_artists: List[CustomerFollowedArtistSchema]

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class FollowersSchema(BaseModel):
    """Schema for representing a list of Customers that follow an artist."""
    followers: List[CustomerSchema]

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class TopFollowersSchema(BaseModel):
    """Schema for representing Artists with most followers."""
    artists: List[ArtistSchema]
    total_followers: int

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True
