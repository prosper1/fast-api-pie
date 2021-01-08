from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    price: float
    is_offer: Optional[bool] = None

@app.get("/")
async def read_root():
    return {"hello":"world"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q:Optional[str] = None):
    return {"item_id":item_id,"q":q}

@app.get("/pie:{pie_name}")
async def get_pie(Item):
    return Item