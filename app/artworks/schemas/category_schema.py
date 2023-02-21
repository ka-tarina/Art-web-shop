from typing import List

from pydantic import UUID4, BaseModel

from app.artworks.schemas import ArtworkSchema


class CategoryBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: UUID4
    artworks: List["ArtworkSchema"] = []

    class Config:
        orm_mode = True
