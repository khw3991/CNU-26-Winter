from fastapi import FastAPI

from app.week2.practice1 import router as practice1_router
from app.week2.practice2 import router as practice2_router
from app.week2.practice3 import router as practice3_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/items/{item}")
async def create_item(item: str):
    return {"item": item}

app.include_router(practice1_router)
app.include_router(practice2_router)
app.include_router(practice3_router)