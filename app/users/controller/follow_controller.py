from fastapi import HTTPException
from app.users.services import FollowServices


class FollowController:
    @staticmethod
    def follow_artist(customer_id: str, artist_id: str):
        try:
            return FollowServices.follow_artist(customer_id, artist_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def unfollow_artist(customer_id: str, artist_id: str):
        try:
            return FollowServices.unfollow_artist(customer_id, artist_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_following_artists(customer_id: str):
        try:
            return FollowServices.get_following_artists(customer_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_followers(artist_id: str):
        try:
            return FollowServices.get_followers(artist_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
