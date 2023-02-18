from typing import List
from pydantic import BaseModel
from app.artworks.models import Artwork


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: str
    artworks: List[Artwork] = []

    class Config:
        orm_mode = True
