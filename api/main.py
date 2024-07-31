from fastapi import FastAPI

from api.db.base import engine, Base
from api.routers import items

# Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def hello():
    return "Hello, Items!123"


app.include_router(items.router)
