"""Module for artwork repository."""
from uuid import uuid4
from sqlalchemy.orm import Session
from app.artworks.models import Artwork


class ArtworkRepository:
    """A repository class for Artwork models."""
    def __init__(self, db: Session):
        """Initializes a new instance of the ArtworkRepository class."""
        self.db = db

    def get_all_artworks(self):
        """Gets all artworks from the database."""
        return self.db.query(Artwork).all()

    def get_artwork_by_id(self, artwork_id: str):
        """Gets an artwork from the database by its id."""
        return self.db.query(Artwork).filter(Artwork.id == artwork_id).first()

    def get_artwork_by_name(self, name: str):
        """Gets an artwork from the database by its name."""
        return self.db.query(Artwork).filter(Artwork.name == name).first()

    def artwork_exists(self, name: str, description: str):
        """Checks if artwork exists in the database."""
        return (
            self.db.query(Artwork).filter_by(name=name, description=description).first()
            is not None
        )

    def create_artwork(
        self,
        name: str,
        description: str,
        price: float,
        image: str,
        stock: int,
        category_id: uuid4,
        artist_id: uuid4,
    ):
        """Creates a new artwork in the system."""
        try:
            artwork = Artwork(
                name=name,
                description=description,
                price=price,
                image=image,
                stock=stock,
                category_id=category_id,
                artist_id=artist_id,
            )
            self.db.add(artwork)
            self.db.commit()
            self.db.refresh(artwork)
            return artwork
        except IndexError as e:
            raise e
        except Exception as e:
            raise e

    def get_stock_by_id(self, artwork_id: str):
        """Gets the stock of an artwork by its ID."""
        try:
            artwork = self.db.query(Artwork).filter(Artwork.id == artwork_id).first()
            return artwork.stock
        except Exception as e:
            raise e

    def update_artwork(self, artwork_id: str, artwork_attribute: str, value):
        """Updates an attribute of the artwork."""
        allowed_attributes = [
            "name",
            "description",
            "price",
            "image",
            "stock",
            "category_id",
            "status",
            "artist_id",
            "currency",
        ]
        if artwork_attribute not in allowed_attributes:
            raise ValueError(
                f"Invalid field '{artwork_attribute}', allowed fields: {allowed_attributes}"
            )
        artwork = self.get_artwork_by_id(artwork_id)
        if artwork:
            setattr(artwork, artwork_attribute, value)
            self.db.commit()
            self.db.refresh(artwork)
            return artwork
        return None

    def get_artworks_in_price_range(self, min_price: float, max_price: float):
        """Returns a list of artworks within the given price range."""
        artworks = (
            self.db.query(Artwork)
            .filter(Artwork.price >= min_price, Artwork.price <= max_price)
            .all()
        )
        if not artworks:
            return None
        return artworks

    def delete_artwork_by_id(self, artwork_id: str):
        """Deletes an artwork from the database by their ID."""
        artwork = self.get_artwork_by_id(artwork_id)
        if not artwork:
            return None
        self.db.delete(artwork)
        self.db.commit()
