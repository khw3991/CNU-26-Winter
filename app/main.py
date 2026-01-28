from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = [
    {'id':1, 'data':'apple', 'rating':3},
    {'id':2, 'data':'banana', 'rating': 4},
    {'id':3, 'data':'cherry', 'rating' : 5}
]

class ItemCreate(BaseModel):
    data: str
    rating: float


@app.post('/items')
def create_item(payload: ItemCreate):
    item = {'id': len(items)+1, **payload.model_dump()}
    items.append(item)
    return item

@app.get('/items')
def get_items(q :float | None=None):
    if q == None :
        return {"data": items}
    result=[]
    for item in items :
        if item.get('rating')>=q :
            result.append(item)
    if len(result)==0 :
        raise HTTPException(status_code=404, detail='Item not found')
    return result

@app.get('/items/{item_id}')
def get_item_by_id(item_id: int):
    for item in items:
        if item.get('id') == item_id:
            return item
    raise HTTPException(status_code=404, detail='Item not found')

