"""Module for superuser schemas."""
from pydantic import UUID4, BaseModel, EmailStr
from app.users.enums import UserRole, UserStatus


class SuperUserSchema(BaseModel):
    """Base model for representing a Superuser."""

    id: UUID4
    username: str
    email: str
    password: str
    status: UserStatus = UserStatus.ACTIVE
    role: UserRole = UserRole.SUPERUSER

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class SuperUserSchemaIn(BaseModel):
    """A schema representing a Superuser creation request"""

    username: str
    email: EmailStr
    password: str

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True
