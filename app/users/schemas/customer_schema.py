from typing import List
from pydantic import UUID4, BaseModel

from app.users.models import UserStatus


class CustomerSchemaBase(BaseModel):
    """Base schema for representing a Customer."""
    name: str
    email: str


class CustomerSchemaCreate(CustomerSchemaBase):
    """A schema representing a Customer creation request"""
    password: str


class CustomerSchemaUpdate(BaseModel):
    """A schema representing a Customer status update request"""
    status: UserStatus


class CustomerSchemaInDB(CustomerSchemaBase):
    """A schema representing a Customer in the database"""
    id: UUID4
    is_verified: bool

    class Config:
        orm_mode = True


# class CustomerSchemaOut(BaseModel):
#     """A schema representing a Customer to return as response"""
#     customer: CustomerSchemaInDB
#     collections: List[CollectionSchemaInDB]
#     orders: List[OrderSchemaInDB]
#     following: List[ArtistSchemaInDB]
#
#     class Config:
#         orm_mode = True
