"""Module for artist controller."""
from uuid import uuid4
from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy.exc import IntegrityError

from app.users.exceptions import UserNotFoundError
from app.users.services import ArtistServices


class ArtistController:
    @staticmethod
    def create_artist(username: str,
                      email: EmailStr,
                      password: str,
                      bio: str = "",
                      website: str = ""):
        """Creates a new artist in the system with error processing."""
        try:
            return ArtistServices.create_artist(username,
                                                email,
                                                password,
                                                bio,
                                                website)
        except IntegrityError:
            raise HTTPException(status_code=409, detail="User already exists")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_artist_by_id(artist_id: str):
        """Gets an artist from the database by their ID."""
        try:
            artist = ArtistServices.get_artist_by_id(artist_id)
            if not artist:
                raise UserNotFoundError(code=404, message="Artist not found")
            return artist
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_artist_by_username(username: str):
        """Gets an artist from the database by their username."""
        try:
            artist = ArtistServices.get_artist_by_username(username)
            if not artist:
                raise UserNotFoundError(code=404, message="Artist not found")
            return artist
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_artists():
        """Gets all artists from the database."""
        try:
            return ArtistServices.get_all_artists()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_artist_bio(artist_id: uuid4, bio: str):
        """Updates bio of an artist."""
        try:
            ArtistServices.update_artist_bio(artist_id, bio)
            return {"detail": "Artist bio updated successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_artist_website(artist_id: uuid4, website: str):
        """Updates website of an artist."""
        try:
            ArtistServices.update_artist_bio(artist_id, website)
            return {"detail": "Artist bio updated successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_artist_by_id(artist_id: str):
        """Deletes an artist from the database by their ID."""
        try:
            deleted = ArtistServices.delete_artist_by_id(artist_id)
            if not deleted:
                raise UserNotFoundError(code=404, message="Artist not found")
            return {"detail": "Artist deleted successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
