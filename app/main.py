from fastapi import FastAPI, HTTPException, APIRouter
from app.items_router import items_router
from app.students_router import Students_router

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router=items_router)
app.include_router(router=Students_router)
