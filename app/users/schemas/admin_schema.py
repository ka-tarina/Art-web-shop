"""Module for admin schemas."""
from pydantic import UUID4, BaseModel, EmailStr
from app.users.enums import UserRole, UserStatus


class AdminSchema(BaseModel):
    """A schema representing an Admin stored in the database"""

    id: UUID4
    username: str
    email: str
    password: str
    status: UserStatus = UserStatus.ACTIVE
    role: UserRole = UserRole.ADMIN

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class AdminSchemaIn(BaseModel):
    """A schema representing an Admin creation request"""

    username: str
    email: EmailStr
    password: str

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True
