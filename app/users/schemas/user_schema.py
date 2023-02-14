from pydantic import BaseModel, UUID4, EmailStr
# Maybe redundant

class UserSchema(BaseModel):
    """Model for representing a User in the system."""
    id: UUID4
    name: str
    email: str
    password: str
    is_active: bool
    is_superuser: bool
    is_admin: bool
    is_artist: bool

    class Config:
        orm_mode = True


class UserSchemaIn(BaseModel):
    """Model for representing incoming user data."""
    name: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class UserSchemaOut(BaseModel):
    """Model for representing user data."""
    id: UUID4
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True
