from pydantic import UUID4, BaseModel, EmailStr
from pydantic.schema import Optional

from app.users.enums import UserRole, UserStatus


class ArtistSchema(BaseModel):
    """Base model for representing an Artist."""
    id: UUID4
    username: str
    email: EmailStr
    bio: str
    website: str
    status: UserStatus
    role: UserRole

    class Config:
        orm_mode = True


class ArtistSchemaUpdate(BaseModel):
    """Model for updating an Artist."""
    id: UUID4
    email: Optional[EmailStr]
    password: Optional[str]
    bio: Optional[str]
    website: Optional[str]

    class Config:
        orm_mode = True


class ArtistSchemaIn(BaseModel):
    """Model for representing incoming Artist data."""
    username: str
    email: EmailStr
    password: str
    bio: str = ""
    website: str = ""

    class Config:
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
        orm_mode = True
