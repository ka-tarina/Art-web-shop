from fastapi import APIRouter, Depends

from app.artworks.controller import ArtworkController, CategoryController
from app.artworks.schemas import ArtworkSchema, ArtworkSchemaIn, ArtworkSchemaUpdate

category_router = APIRouter(tags=["categories"], prefix="/api/category")


@category_router.post("/create-new-category")
async def create_category(name: str):
    return CategoryController.create_new_category(name)


@category_router.get("/get-all-categories")
async def get_all_categories():
    return CategoryController.get_all_categories()


@category_router.get("/get-category-by-id/{category_id}")
async def get_category_by_id(category_id: str):
    return CategoryController.get_category_by_id(category_id)


@category_router.get("/get-category_by_name")
async def get_category_by_name(name: str):
    return CategoryController.get_category_by_name(name)


@category_router.delete("/delete-category")
async def delete_category_by_id(category_id: str):
    return CategoryController.delete_category_by_id(category_id)


@category_router.put("/update-category-name/{category_id}")
async def update_category_name(category_id: str, new_name: str):
    return CategoryController.update_category_name(category_id, new_name)


@category_router.get("/get-artworks-by-category-name/{category_name}/artworks")
async def get_artworks_by_category_name(
    category_name: str, skip: int = 0, limit: int = 100
):
    return CategoryController.get_artworks_by_category_name(category_name, skip, limit)


@category_router.get("/get-artworks-by-category-id/{category_id}/artworks")
async def get_artworks_by_category_id(
    category_id: str, skip: int = 0, limit: int = 100
):
    return CategoryController.get_artworks_by_category_id(category_id, skip, limit)


artwork_router = APIRouter(tags=["artworks"], prefix="/api/artworks")


@artwork_router.post("/create-new-artwork", response_model=ArtworkSchema)
def create_new_artwork(artwork: ArtworkSchemaIn):
    return ArtworkController.create_new_artwork(
        artwork.name,
        artwork.description,
        artwork.price,
        artwork.image,
        artwork.stock,
        artwork.category_id,
        artwork.status,
        artwork.artist_id,
        artwork.currency,
    )


@artwork_router.get("/get-all-artworks", response_model=list[ArtworkSchema])
def get_all_artworks():
    return ArtworkController.get_all_artworks()


@artwork_router.get("/get-artwork-by-id/{artwork_id}", response_model=ArtworkSchema)
def get_artwork_by_id(artwork_id: str):
    return ArtworkController.get_artwork_by_id(artwork_id)


@artwork_router.get(
    "/get-artwork-by-name/{artwork_name}", response_model=list[ArtworkSchema]
)
def get_artwork_by_name(artwork_name: str):
    return ArtworkController.get_artwork_by_name(artwork_name)


@artwork_router.get("/{artwork_id}/stock", response_model=int)
def get_stock_by_artwork_id(artwork_id: str):
    return ArtworkController.get_stock_by_artwork_id(artwork_id)


@artwork_router.delete("/delete_artwork_by_id/{artwork_id}", status_code=204)
def delete_artwork_by_id(artwork_id: str):
    return ArtworkController.delete_artwork_by_id(artwork_id)


@artwork_router.put("/update_artwork/{artwork_id}")
def update_artwork(artwork_id: str, artwork_data: ArtworkSchemaUpdate):
    return ArtworkController.update_artwork(
        artwork_id, artwork_data.attribute, artwork_data.value
    )


@artwork_router.get("/get-artworks-in-price-range")
def get_artworks_in_price_range(min_price: float, max_price: float):
    return ArtworkController.get_artworks_in_price_range(min_price, max_price)
