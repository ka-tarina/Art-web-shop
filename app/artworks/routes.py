"""
API for artwork management. It includes routes for
creating, deleting and updating artwork and categories.
"""
from fastapi import APIRouter
from app.artworks.controller import ArtworkController, CategoryController
from app.artworks.schemas import (
    ArtworkSchema,
    ArtworkSchemaIn,
    ArtworkSchemaUpdate,
    CategoryArtworksSchema
)
from app.artworks.schemas import CategorySchema, CategorySchemaIn, CategorySchemaUpdate

category_router = APIRouter(tags=["categories"], prefix="/api/category")


@category_router.post("/create-new-category",
                      response_model=CategorySchema)
async def create_category(category: CategorySchemaIn):
    """Creates a new category"""
    return CategoryController.create_new_category(category.name)


@category_router.get("/get-all-categories",
                     response_model=list[CategorySchema])
async def get_all_categories():
    """Retrieves all categories."""
    return CategoryController.get_all_categories()


@category_router.get("/get-category-by-id/{category_id}",
                     response_model=CategorySchema)
async def get_category_by_id(category_id: str):
    """Retrieves a category by id."""
    return CategoryController.get_category_by_id(category_id)


@category_router.get("/get-category_by_name",
                     response_model=CategorySchema)
async def get_category_by_name(name: str):
    """Retrieves a category by name."""
    return CategoryController.get_category_by_name(name)


@category_router.delete("/delete-category")
async def delete_category_by_id(category_id: str):
    """Deletes category by id."""
    return CategoryController.delete_category_by_id(category_id)


@category_router.put("/update-category-name/{category_id}",
                     response_model=CategorySchema)
async def update_category_name(category: CategorySchemaUpdate):
    """Updates a category name by id."""
    return CategoryController.update_category_name(category.id, category.name)


artwork_router = APIRouter(tags=["artworks"], prefix="/api/artworks")


@artwork_router.post("/create-new-artwork", response_model=ArtworkSchema)
def create_new_artwork(artwork: ArtworkSchemaIn):
    """Creates a new artwork."""
    return ArtworkController.create_new_artwork(
        artwork.name,
        artwork.description,
        artwork.price,
        artwork.image,
        artwork.stock,
        artwork.category_id,
        artwork.artist_id,
    )


@artwork_router.get("/get-all-artworks", response_model=list[ArtworkSchema])
def get_all_artworks():
    """Retrieves all artworks"""
    return ArtworkController.get_all_artworks()


@artwork_router.get("/get-artwork-by-id/{artwork_id}", response_model=ArtworkSchema)
def get_artwork_by_id(artwork_id: str):
    """Retrieves an artwork by id"""
    return ArtworkController.get_artwork_by_id(artwork_id)


@artwork_router.get(
    "/get-artwork-by-name/{artwork_name}", response_model=ArtworkSchema
)
def get_artwork_by_name(artwork_name: str):
    """Retrieves artworks by name"""
    return ArtworkController.get_artwork_by_name(artwork_name)


@artwork_router.get("/{artwork_id}/stock", response_model=int)
def get_stock_by_artwork_id(artwork_id: str):
    """Retrieves the stock of an artwork by id"""
    return ArtworkController.get_stock_by_artwork_id(artwork_id)


@artwork_router.delete("/delete_artwork_by_id/{artwork_id}", status_code=204)
def delete_artwork_by_id(artwork_id: str):
    """Deletes an artwork by id"""
    return ArtworkController.delete_artwork_by_id(artwork_id)


@artwork_router.put("/update_artwork/{artwork_id}")
def update_artwork(artwork_id: str, artwork_data: ArtworkSchemaUpdate):
    """Updates an artwork by id"""
    return ArtworkController.update_artwork(
        artwork_id, artwork_data.attribute, artwork_data.value
    )


@artwork_router.get("/get-artworks-in-price-range")
def get_artworks_in_price_range(min_price: float, max_price: float):
    """Retrieves artworks within a price range"""
    return ArtworkController.get_artworks_in_price_range(min_price, max_price)


@artwork_router.get("/get-artworks-by-category-id/{category_id}/artworks",
                    response_model=CategoryArtworksSchema)
async def get_artworks_by_category_id(category_id: str, skip: int = 0, limit: int = 100):
    """Retrieves artworks by category id"""
    return CategoryController.get_artworks_by_category_id(category_id,  skip, limit)


@artwork_router.get("/get-artworks-by-category-name/{category_name}/artworks",
                    response_model=CategoryArtworksSchema)
async def get_artworks_by_category_name(category_name: str, skip: int = 0, limit: int = 100):
    """Retrieves artworks by category name"""
    return CategoryController.get_artworks_by_category_name(category_name, skip, limit)
