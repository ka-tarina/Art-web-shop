from enum import Enum
from pydantic import BaseModel, UUID4


class Currency(str, Enum):
    RSD = "RSD"
    EUR = "EUR"


class ArtworkBase(BaseModel):
    name: str
    description: str
    price: float
    image: str
    stock: int
    category_id: UUID4
    status: bool
    artist_id: UUID4
    currency: Currency

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ArtworkCreate(ArtworkBase):
    pass


class Artwork(ArtworkBase):
    id: UUID4

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
