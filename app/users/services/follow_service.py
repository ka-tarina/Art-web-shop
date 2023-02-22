from app.db.database import SessionLocal
from app.users.repository import FollowRepository


def repository_method_wrapper(func):
    def wrapper(*args, **kwargs):
        with SessionLocal() as db:
            try:
                repository = FollowRepository(db)
                return func(repository, *args, **kwargs)
            except Exception as e:
                raise e
    return wrapper


class FollowServices:
    @staticmethod
    @repository_method_wrapper
    def follow_artist(repository, customer_id, artist_id):
        """Allows a customer to follow an artist"""
        return repository.follow_artist(customer_id, artist_id)

    @staticmethod
    @repository_method_wrapper
    def unfollow_artist(repository, customer_id, artist_id):
        """Allows a customer to unfollow an artist"""
        return repository.unfollow_artist(customer_id, artist_id)

    @staticmethod
    @repository_method_wrapper
    def get_following_artists(repository, customer_id):
        """Retrieves all artists that a customer is following."""
        return repository.get_following_artists(customer_id)

    @staticmethod
    @repository_method_wrapper
    def get_followers(repository, artist_id):
        """Retrieves all customers who are following an artist."""
        return repository.get_followers(artist_id)

    @staticmethod
    @repository_method_wrapper
    def get_artists_by_followers(repository, limit):
        """Retrieves the top N artists with the most followers."""
        return repository.get_artists_by_followers(limit)
