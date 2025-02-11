import os

from fastapi import FastAPI

from .database import engine
from .models import Base
from .urls import urls

ENV = os.getenv("ENV")

app = FastAPI()

Base.metadata.create_all(engine)

if ENV == "testing":
    con = engine.connect()
    trans = con.begin()
    for tbl in reversed(Base.metadata.sorted_tables):
        con.execute(tbl.delete())
    trans.commit()

app.include_router(urls.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
