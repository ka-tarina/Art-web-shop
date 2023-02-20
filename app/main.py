import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from app.db.database import Base, engine
from app.users.routes import user_router, customer_router, superuser_router, artist_router, admin_router, follow_router
from app.artworks.routes import category_router, artwork_router
from app.orders.routes import order_router
from celery import Celery

Base.metadata.create_all(bind=engine)


def init_app():
    app = FastAPI()
    # app.include_router(user_router)
    app.include_router(category_router)
    app.include_router(artwork_router)
    app.include_router(customer_router)
    app.include_router(superuser_router)
    app.include_router(artist_router)
    app.include_router(admin_router)
    app.include_router(follow_router)
    app.include_router(order_router)
    return app


app = init_app()


@app.get("/", include_in_schema=False)
def hello_world():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run(app)
