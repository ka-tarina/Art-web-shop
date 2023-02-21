from typing import Optional

from pydantic import UUID4, BaseModel, EmailStr

from app.users.enums import UserRole, UserStatus


class SuperUserSchema(BaseModel):
    """Base model for representing a Superuser."""

    id: UUID4
    name: str
    email: str
    password: str
    status: UserStatus = UserStatus.ACTIVE
    role: UserRole = UserRole.SUPERUSER

    class Config:
        orm_mode = True


class SuperUserSchemaIn(BaseModel):
    """A schema representing a Superuser creation request"""

    name: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
