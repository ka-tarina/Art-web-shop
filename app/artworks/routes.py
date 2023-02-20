from fastapi import APIRouter
from app.artworks.controller import CategoryController

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
