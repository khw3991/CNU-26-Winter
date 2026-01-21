from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter(prefix="/week2/practice2", tags=["week2"])

class MemoCreate(BaseModel):
    title: str
    content: str

MEMOS = []
NEXT_ID = 1

@router.post('/memos', status_code=201)
def create_memo(payload: MemoCreate):
    global NEXT_ID
    memo = {'id': NEXT_ID, **payload.model_dump()}
    MEMOS.append(memo)
    NEXT_ID += 1
    return memo