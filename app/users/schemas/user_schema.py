"""Module for user schemas."""
from pydantic import BaseModel, UUID4, EmailStr

from app.users.enums import UserStatus, UserRole


class UserSchema(BaseModel):
    """Model for representing a User in the system."""
    id: UUID4
    username: str
    email: str
    password: str
    status: UserStatus
    role: UserRole

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class UserSchemaIn(BaseModel):
    """Model for representing incoming user data."""
    name: str
    email: EmailStr
    password: str

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class UserSchemaOut(BaseModel):
    """Model for representing user data."""
    id: UUID4
    name: str
    email: str
    password: str

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class UserSchemaUpdate(BaseModel):
    """Model for representing user data."""
    id: str
    role: UserRole

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class LoginSchema(BaseModel):
    """Schema for user login."""
    email: str
    password: str
