from typing import List
from pydantic import BaseModel, UUID4
from app.artworks.schemas import ArtworkBase


class CategoryBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: UUID4
    artworks: List["ArtworkBase"] = []

    class Config:
        orm_mode = True
