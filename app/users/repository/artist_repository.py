from sqlalchemy.orm import Session
from app.users.models import Artist, UserStatus


class ArtistRepository:
    """A repository class for performing CRUD operations on Artist models."""

    def __init__(self, db: Session):
        """Initializes a new instance of the ArtistRepository class."""
        self.db = db

    def create_artist(self, username: str, email: str, password: str, bio: str = "", website: str = ""):
        """Creates a new artist in the system."""
        try:
            artist = Artist(username=username, email=email, password=password, status=UserStatus.ACTIVE, bio=bio,
                            website=website)
            self.db.add(artist)
            self.db.commit()
            self.db.refresh(artist)
            return artist
        except Exception as e:
            raise e

    def get_artist_by_id(self, artist_id: str):
        """Gets an artist from the database by their ID."""
        artist = self.db.query(Artist).get(artist_id)
        if artist is None:
            raise Exception(f"Artist with ID {artist_id} not found")
        return artist

    def get_artist_by_username(self, username: str):
        """Gets an artist from the database by their ID."""
        artist = self.db.query(Artist).get(username)
        if artist is None:
            raise Exception(f"Artist with username {username} not found")
        return artist

    def get_all_artists(self):
        """Gets all artists from the database."""
        return self.db.query(Artist).all()

    def update_artist_bio(self, artist_id: str, bio: str):
        """Updates the bio of an existing artist in the system."""
        try:
            artist = self.get_artist_by_id(artist_id)
            artist.bio = bio
            self.db.commit()
            self.db.refresh(artist)
            return artist
        except Exception as e:
            raise e

    def update_artist_website(self, artist_id: str, website: str) -> Artist:
        """Updates the website of an existing artist in the system."""
        try:
            artist = self.get_artist_by_id(artist_id)
            artist.website = website
            self.db.commit()
            self.db.refresh(artist)
            return artist
        except Exception as e:
            raise e

    def delete_artist(self, artist_id: str):
        """Deletes an artist from the system."""
        try:
            artist = self.get_artist_by_id(artist_id)

            self.db.delete(artist)
            self.db.commit()
            return True
        except Exception as e:
            raise e
