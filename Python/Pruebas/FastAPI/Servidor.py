from typing import Union
from fastapi import FastAPI
from empleats import empleats

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"Alumnes"}


@app.get("/items/{item_id}" )
def read_item(item_id: int, q: Union[str, None] = None):
     return {"item_id": item_id, "q": q}
