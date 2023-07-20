from typing import Union
from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
  name: str
  price: float
  is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
  return {"item_name": item.price, "item_id": item_id}


# If you have a path operation that receives a path parameter, but you want the possible valid path parameter values to be predefined, you can use a standard Python Enum
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# QUERY PARAMETERS
# you can declare fn parameters that aren't part of path parameters -- automatically interpreted as "query" parameter

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
# http://127.0.0.1:8000/items/
# would be the same as going to:
# http://127.0.0.1:8000/items/?skip=0&limit=10

# http://127.0.0.1:8000/items/?skip=20 would be skip = 20 and limit = 10 since you set it in the URL

# OPTIONAL PARAMETERS
# can declare optional query parameters by setting their default to None

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

# fn parameter q will be optional, and will be None by default.
# can set REQUIRED parameters