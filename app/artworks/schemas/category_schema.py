"""Module for category schemas."""
from typing import List
from pydantic import UUID4, BaseModel
from app.artworks.schemas import ArtworkSchema


class CategorySchema(BaseModel):
    """A schema representing a Category stored in the database"""
    id: UUID4
    name: str
    artworks: List[ArtworkSchema] = []

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class CategorySchemaIn(BaseModel):
    """A schema representing a Category creation request"""
    name: str

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class CategorySchemaUpdate(BaseModel):
    """A schema representing a Category update request"""
    id: UUID4
    name: str

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class CategoryArtworksSchema(BaseModel):
    """A schema representing a Category with a list of Artworks."""
    name: str
    artworks: List[ArtworkSchema] = []

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True
