"""Module for follow repository."""
from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.users.models import Artist, Customer


class FollowRepository:
    """A repository class for Follow models."""
    def __init__(self, db: Session):
        """Initializes a new instance of the FollowRepository class."""
        self.db = db

    def follow_artist(self, customer_id: str, artist_id: str):
        """Allows a customer to follow an artist."""
        try:
            customer = self.db.query(Customer).get(customer_id)
            artist = self.db.query(Artist).get(artist_id)
            if artist not in customer.following:
                customer.following.append(artist)
                artist.followers.append(customer)
                self.db.commit()
                self.db.refresh(customer)
            return customer
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def unfollow_artist(self, customer_id: str, artist_id: str) -> Customer:
        """Allows a customer to unfollow an artist."""
        try:
            customer = self.db.query(Customer).get(customer_id)
            artist = self.db.query(Artist).get(artist_id)
            if artist in customer.following:
                customer.following.remove(artist)
                artist.followers.remove(customer)
                self.db.commit()
                self.db.refresh(customer)
            return customer
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def get_following_artists(self, customer_id: str):
        """Retrieves all artists that a customer is following."""
        try:
            customer = self.db.query(Customer).get(customer_id)
            return customer.following
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def get_followers(self, artist_id: str):
        """Retrieves all customers who are following an artist."""
        try:
            artist = self.db.query(Artist).get(artist_id)
            return artist.followers
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def get_artists_by_followers(self, limit: int = 10):
        """Retrieves the top N artists with the most followers."""
        try:
            artists = self.db.query(Artist).order_by(desc(Artist.num_followers)).limit(limit).all()
            return artists
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e
