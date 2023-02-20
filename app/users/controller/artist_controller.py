from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy.exc import IntegrityError
from app.users.services import ArtistServices
from app.users.enums import UserStatus


class ArtistController:
    @staticmethod
    def create_artist(email: EmailStr, username: str, password: str):
        try:
            return ArtistServices.create_artist(email, username, password, status=UserStatus.PENDING)
        except IntegrityError:
            raise HTTPException(status_code=409, detail="User already exists")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_artist_by_id(artist_id: str):
        try:
            artist = ArtistServices.get_artist_by_id(artist_id)
            if not artist:
                raise HTTPException(status_code=404, detail="Artist not found")
            return artist
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_artist_by_username(username: str):
        try:
            artist = ArtistServices.get_artist_by_id(username)
            if not artist:
                raise HTTPException(status_code=404, detail="Artist not found")
            return artist
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_artists():
        try:
            return ArtistServices.get_all_artists()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_artist_bio(artist_id: str, bio: str):
        try:
            ArtistServices.update_artist_bio(artist_id, bio)
            return {"detail": "Artist bio updated successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_artist_website(artist_id: str, website: str):
        try:
            ArtistServices.update_artist_bio(artist_id, website)
            return {"detail": "Artist bio updated successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_artist_by_id(artist_id: str):
        try:
            deleted = ArtistServices.delete_artist_by_id(artist_id)
            if not deleted:
                raise HTTPException(status_code=404, detail="Artist not found")
            return {"detail": "Artist deleted successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
