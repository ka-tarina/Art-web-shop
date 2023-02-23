"""Module for artwork controller."""
from uuid import uuid4
from fastapi import HTTPException, Response
from app.artworks.exceptions import ArtworkExceptionCode, ArtworkNotFoundException
from app.artworks.schemas import Currency
from app.artworks.services import ArtworkService


class ArtworkController:
    """A controller for handling requests related to artwork."""
    @staticmethod
    def create_new_artwork(
        name: str,
        description: str,
        price: float,
        image: str,
        stock: str,
        category_id: uuid4,
        status: bool,
        artist_id: uuid4,
        currency: Currency,
    ):
        """Creates a new artwork in the system."""
        try:
            artwork = ArtworkService.create_artwork(
                name=name,
                description=description,
                price=price,
                image=image,
                stock=stock,
                category_id=category_id,
                status=status,
                artist_id=artist_id,
                currency=currency,
            )
            return artwork
        except ArtworkExceptionCode as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_artworks():
        """Gets all artworks from the database."""
        artworks = ArtworkService.get_all_artworks()
        return artworks

    @staticmethod
    def get_artwork_by_id(artwork_id: str):
        """Gets an artwork from the database by its ID."""
        try:
            artwork = ArtworkService.get_artwork_by_id(artwork_id)
            return artwork
        except ArtworkNotFoundException as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_artwork_by_name(artwork_name: str):
        """Gets an artwork from the database by its name."""
        try:
            artwork = ArtworkService.get_artwork_by_name(artwork_name)
            return artwork
        except ArtworkNotFoundException as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_stock_by_artwork_id(artwork_id):
        """Gets stock of an artwork from the database by its id."""
        try:
            artwork = ArtworkService.get_artwork_by_id(artwork_id)
            if not artwork:
                raise ArtworkNotFoundException(
                    f"Artwork with ID {artwork_id} not found.", code=400
                )
            return ArtworkService.get_stock_by_artwork_id(artwork_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_artwork_by_id(artwork_id: str):
        """Deletes an artwork from the database by their ID."""
        try:
            ArtworkService.delete_artwork_by_id(artwork_id)
            return Response(
                content=f"Artwork with provided ID {artwork_id} was successfully deleted.",
                status_code=200,
            )
        except ArtworkNotFoundException as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_artwork(artwork_id: str, artwork_attribute: str, value):
        """Updates an attribute of the artwork."""
        try:
            artwork = ArtworkService.update_artwork(
                artwork_id=artwork_id, artwork_attribute=artwork_attribute, value=value
            )
            return artwork
        except ArtworkNotFoundException as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_artworks_in_price_range(min_price: float, max_price: float):
        """Returns a list of artworks within the given price range."""
        try:
            artworks = ArtworkService.get_artworks_in_price_range(
                min_price=min_price, max_price=max_price
            )
            return artworks
        except Exception as e:
            raise Exception(f"Error retrieving artworks: {str(e)}")
