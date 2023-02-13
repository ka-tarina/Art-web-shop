import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from app.db.database import Base, engine
from app.users.routes import user_router

Base.metadata.create_all(bind=engine)


def init_app():
    app = FastAPI()
    app.include_router(user_router)
    return app


app = init_app()


@app.get("/", include_in_schema=False)
def hello_world():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run(app)
