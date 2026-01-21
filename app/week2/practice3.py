from fastapi import HTTPException
from fastapi import APIRouter
from app.week2.practice2 import MEMOS

router = APIRouter(prefix="/week2/practice3", tags=["week2"])

@router.get('/memos')
def list_memos():
    return MEMOS

@router.get('/memos/{memo_id}')
def read_memo(memo_id: int):
    for memo in MEMOS:
        if memo['id'] == memo_id:
            return memo
    raise HTTPException(status_code=404, detail='Memo not found')