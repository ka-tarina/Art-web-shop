"""Module for artist schemas."""
from pydantic import UUID4, BaseModel, EmailStr
from pydantic.schema import Optional
from app.users.enums import UserRole, UserStatus


class ArtistSchema(BaseModel):
    """A schema representing an Admin stored in the database"""
    id: UUID4
    username: str
    email: EmailStr
    bio: str
    website: str
    status: UserStatus
    role: UserRole

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class ArtistSchemaUpdate(BaseModel):
    """Model for updating an Artist."""
    id: str
    email: Optional[EmailStr]
    password: Optional[str]
    bio: Optional[str]
    website: Optional[str]

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class ArtistSchemaIn(BaseModel):
    """Model for representing incoming Artist data."""
    username: str
    email: EmailStr
    password: str
    bio: str = ""
    website: str = ""

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class ArtistSchemaOut(BaseModel):
    """Model for representing outgoing Artist data."""
    username: str
    email: EmailStr
    bio: str
    website: str
    status: UserStatus
    role: UserRole

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True
