from pydantic import BaseModel, UUID4


class ArtistSchema(BaseModel):
    """Model for representing an Artist in the system."""
    id: UUID4
    user_id: str
    status: str
