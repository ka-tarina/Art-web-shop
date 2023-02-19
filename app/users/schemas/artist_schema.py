from pydantic import UUID4, BaseModel, EmailStr
from app.users.models import UserRole, UserStatus


class ArtistSchemaBase(BaseModel):
    """Base model for representing an Artist."""
    id: UUID4
    name: str
    email: EmailStr
    bio: str
    website: str
    status: UserStatus
    role: UserRole

    class Config:
        orm_mode = True


class ArtistSchemaCreate(BaseModel):
    """Model for creating an Artist."""
    name: str
    email: EmailStr
    password: str
    bio: str = ""
    website: str = ""


class ArtistSchemaUpdate(BaseModel):
    """Model for updating an Artist."""
    name: str
    email: EmailStr
    password: str
    bio: str = ""
    website: str = ""


class ArtistSchemaIn(ArtistSchemaCreate):
    """Model for representing incoming Artist data."""

    class Config:
        orm_mode = True


class ArtistSchemaOut(ArtistSchemaBase):
    """Model for representing outgoing Artist data."""

    class Config:
        orm_mode = True
