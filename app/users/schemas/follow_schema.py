from pydantic import UUID4, BaseModel
from pydantic.schema import Optional, List
from app.users.schemas import ArtistSchema, CustomerSchema


class CustomerFollowedArtistSchema(BaseModel):
    customer_id: UUID4
    artist_id: UUID4
    username: str
    bio: Optional[str]

    class Config:
        orm_mode = True


class FollowSchema(BaseModel):
    customer_id: UUID4
    artist_id: UUID4

    class Config:
        orm_mode = True


class FollowingArtistsSchema(BaseModel):
    following_artists: List[CustomerFollowedArtistSchema]

    class Config:
        orm_mode = True


class FollowersSchema(BaseModel):
    followers: List[CustomerSchema]

    class Config:
        orm_mode = True


class TopFollowersSchema(BaseModel):
    artists: List[ArtistSchema]
    total_followers: int

    class Config:
        orm_mode = True
