"""Model for follow controller"""
from uuid import uuid4

from fastapi import HTTPException
from app.users.schemas import ArtistSchema
from app.users.services import FollowServices


class FollowController:
    @staticmethod
    def follow_artist(customer_id: uuid4, artist_id: uuid4):
        """Follow an artist with the specified IDs."""
        try:
            return FollowServices.follow_artist(customer_id, artist_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def unfollow_artist(customer_id: uuid4, artist_id: uuid4):
        """Unfollow an artist with the specified IDs"""
        try:
            return FollowServices.unfollow_artist(customer_id, artist_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_following_artists(customer_id: uuid4):
        """Get the artists that a customer is following."""
        try:
            return FollowServices.get_following_artists(customer_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_followers(artist_id: uuid4):
        """Get the followers of an artist with the specified ID."""
        try:
            return FollowServices.get_followers(artist_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_artists_by_followers(limit: int):
        """Get a list of artists with the number of followers, sorted by the number of followers."""
        try:
            artists = FollowServices.get_artists_by_followers(limit)
            total_followers = sum(artist.followers for artist in artists)
            return {"artists": [ArtistSchema.from_orm(artist) for artist in artists],
                    "total_followers": total_followers}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
