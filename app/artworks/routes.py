from fastapi import APIRouter, Depends
from app.artworks.controller import CategoryController, ArtworkController
from app.artworks.schemas import ArtworkCreate, ArtworkUpdate

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
async def get_category_by_name(category_name: str):
    return CategoryController.get_category_by_name(category_name)


@category_router.delete("/delete-category")
async def delete_category_by_id(category_id: str):
    return CategoryController.delete_category_by_id(category_id)


@category_router.put("/update-category-name/{category_id}")
async def update_category_name(category_id: str, new_name: str):
    return CategoryController.update_category_name(category_id, new_name)


@category_router.get("/get-artworks-by-category-name/{category_name}/artworks")
async def get_artworks_by_category_name(category_name: str, skip: int = 0, limit: int = 100):
    return CategoryController.get_artworks_by_category_name(category_name, skip, limit)


@category_router.get("/get-artworks-by-category-id/{category_id}/artworks")
async def get_artworks_by_category_id(category_id: str, skip: int = 0, limit: int = 100):
    return CategoryController.get_artworks_by_category_id(category_id, skip, limit)


artwork_router = APIRouter(tags=["artwork"], prefix="/api/artworks")


@artwork_router.post("/", response_model=ArtworkCreate)
def create_artwork(artwork_data: ArtworkCreate, controller: ArtworkController = Depends()):
    return controller.create_new_artwork(**artwork_data.dict())


@artwork_router.get("/", response_model=list[ArtworkCreate])
def get_all_artworks(controller: ArtworkController = Depends()):
    return controller.get_all_artworks()


@artwork_router.get("/{artwork_id}", response_model=ArtworkCreate)
def get_artwork_by_id(artwork_id: str, controller: ArtworkController = Depends()):
    return controller.get_artwork_by_id(artwork_id)


@artwork_router.get("/search/{artwork_name}", response_model=ArtworkCreate)
def get_artwork_by_name(artwork_name: str, controller: ArtworkController = Depends()):
    return controller.get_artwork_by_name(artwork_name)


@artwork_router.get("/{artwork_id}/stock", response_model=int)
def get_stock_by_artwork_id(artwork_id: str, controller: ArtworkController = Depends()):
    return controller.get_stock_by_artwork_id(artwork_id)


@artwork_router.delete("/{artwork_id}", status_code=204)
def delete_artwork_by_id(artwork_id: str, controller: ArtworkController = Depends()):
    return controller.delete_artwork_by_id(artwork_id)


@artwork_router.put("/{artwork_id}", response_model=ArtworkCreate)
def update_artwork(artwork_id: str, artwork_data: ArtworkUpdate, controller: ArtworkController = Depends()):
    return controller.update_artwork(artwork_id, artwork_data.attribute, artwork_data.value)


@artwork_router.get("/search", response_model=list[ArtworkCreate])
def get_artworks_in_price_range(min_price: float, max_price: float, controller: ArtworkController = Depends()):
    return controller.get_artworks_in_price_range(min_price, max_price)
