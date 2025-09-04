from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


items = {}


@app.get("/")
def read_root() -> dict[str, Union[str, int]]:
    return {"message": "Hello, World!", "status": 200}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    if item_id not in items:
        return {"error": "Item not found"}
    # item_details =
    return {"item_id": item_id, "item": items[item_id]}


@app.post("/items/")
def create_item(item: Item) -> dict[str, Union[str, float, None]]:
    item_dict = item.model_dump()
    item_id = item.id
    items[item_id] = item
    return item_dict


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item) -> dict[str, Union[int, str, float, None]]:
    # Update the item in the in-memory storage
    items[item_id] = item
    return {"item_id": item_id, **item.model_dump()}
