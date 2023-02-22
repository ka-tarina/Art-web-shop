from enum import Enum

from pydantic import UUID4, BaseModel
from pydantic.schema import Any


class Currency(str, Enum):
    RSD = "RSD"
    EUR = "EUR"


class ArtworkSchema(BaseModel):
    """A schema representing an Artwork stored in the database"""
    id: UUID4
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


class ArtworkSchemaIn(BaseModel):
    """A schema representing an Artwork creation request"""
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


class ArtworkSchemaUpdate(BaseModel):
    attribute: str
    value: Any

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
