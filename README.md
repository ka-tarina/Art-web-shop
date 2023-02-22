Artist Web Shop Python Project - README

This project provides an API for managing an artist web shop. It is built using the FastAPI framework and uses MySQL for data storage. The following endpoints are available:
Requirements

    mysql-connector-python
    SQLAlchemy==2.0.3
    sqlalchemy-utils
    fastapi[all]==0.91.0
    fastapi-utils
    PYMYSQL~=1.0.2
    uvicorn~=0.20.0
    pydantic~=1.10.4
    cryptography
    PyJWT==2.6.0
    python-decouple~=3.7
    bcrypt
    starlette~=0.24.0
    enum34
    celery~=5.2.7
    redis~=4.5.1
    pre-commit~=3.0.4

Endpoints
Categories
Create a new category

    Endpoint: POST /api/category/create-new-category
    Function: CategoryController.create_category
    Request body: CategoryCreateSchema
    Response: CategorySchema

Get all categories

    Endpoint: GET /api/category/get-all-categories
    Function: CategoryController.get_all_categories
    Response: List[CategorySchema]

Get category by ID

    Endpoint: GET /api/category/get-category-by-id/{category_id}
    Function: CategoryController.get_category_by_id
    Path parameter: category_id - ID of the category to retrieve
    Response: CategorySchema

Get category by name

    Endpoint: GET /api/category/get-category_by_name
    Function: CategoryController.get_category_by_name
    Query parameter: name - name of the category to retrieve
    Response: CategorySchema

Delete category

    Endpoint: DELETE /api/category/delete-category
    Function: CategoryController.delete_category
    Request body: CategoryDeleteSchema
    Response: CategorySchema

Update category name

    Endpoint: PUT /api/category/update-category-name/{category_id}
    Function: CategoryController.update_category_name
    Path parameter: category_id - ID of the category to update
    Request body: CategoryUpdateSchema
    Response: CategorySchema

Get artworks by category name

    Endpoint: GET /api/category/get-artworks-by-category-name/{category_name}/artworks
    Function: CategoryController.get_artworks_by_category_name
    Path parameter: category_name - name of the category to retrieve artworks from
    Response: List[ArtworkSchema]

Get artworks by category ID

    Endpoint: GET /api/category/get-artworks-by-category-id/{category_id}/artworks
    Function: CategoryController.get_artworks_by_category_id
    Path parameter: category_id - ID of the category to retrieve artworks from
    Response: List[ArtworkSchema]

Artworks
Create a new artwork

    Endpoint: POST /api/artworks/create-new-artwork
    Function: ArtworkController.create_artwork
    Request body: ArtworkCreateSchema
    Response: ArtworkSchema

Get all artworks

    Endpoint: GET /api/artworks/get-all-artworks
    Function: ArtworkController.get_all_artworks
    Response: List[ArtworkSchema]

Get artwork by ID

    Endpoint: GET /api/artworks/get-artwork-by-id/{artwork_id}
    Function: `
