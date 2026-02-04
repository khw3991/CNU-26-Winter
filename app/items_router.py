from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: int
    data: str
    rating: float


items = [
    Item(id=1, data='apple', rating=3),
    Item(id=2, data='banana', rating=3),
    Item(id=3, data='cherry', rating=3)
]

items_router=APIRouter(prefix='/items', tags=["items"])


class ItemCreate(BaseModel):
    data: str
    rating: float

class ItemPut(BaseModel):
    data:str
    rating:float

class ItemPatch(BaseModel):
    data : Optional[str]=None
    rating : Optional[float]=None

@items_router.get('/')
def get_items():
    return items

@items_router.post(path='/')
def create_item(payload: ItemCreate):
    item = Item(id=len(items)+1, data=payload.data, rating=payload.rating)
    items.append(item)
    return item

@items_router.delete('/{item_id}')
def remove_item(item_id:int):
    for item in items:
        if item.id==item_id:
            items.remove(item)
            return
    raise HTTPException(status_code=404, detail='Item not found')


@items_router.get('/{item_id}')
def get_item_by_id(item_id: int):
    for item in items:
        if item.id== item_id:
            return item
    raise HTTPException(status_code=404, detail='Item not found')

@items_router.put(path='/{item_id}')
def update_item(payload:ItemPut, item_id :int):
    for item in items:
        if item.id == item_id:
            item.data=payload.data
            item.rating=payload.rating
            return item
    raise HTTPException(status_code=404, detail='Item not found')

@items_router.patch(path='/{item_id}')
def patch_item(payload:ItemPatch, item_id:int):
    for item in items:
        if item.id==item_id:
            if payload.data is not None:
                item.data=payload.data
            if payload.rating is not None:
                item.rating=payload.rating
            return item
    raise HTTPException(status_code=404, detail='Item not found')

