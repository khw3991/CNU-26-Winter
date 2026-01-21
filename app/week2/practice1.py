from fastapi import APIRouter

router = APIRouter(prefix="/week2/practice1", tags=["week2"])

@router.get("/")
def root():
    return {"message": "Hello FastAPI"}


@router.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}


@router.get("/search")
def search(keyword: str):
    return {"keyword": keyword}
