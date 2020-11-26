from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId

app = FastAPI()

client = MongoClient(port=27017)
db = client.todolist


class Item(BaseModel):
    user: str
    task: str
    date: datetime.date
    time: datetime.time
    tags: Optional[List[str]]


@app.post("/items")
def create_item(item: Item):
    return {"item_id": str(db.items.insert_one(dict(item)).inserted_id)}


@app.get("/items/{item_id}")
def read_item(item_id: str):
    item = db.items.find_one({"_id": ObjectId(item_id)})
    item["_id"] = str(item["_id"])
    return item


@app.get("/items")
def read_items(user: Optional[str] = None, tags: Optional[str] = None):
    filter = {}
    if user:
        filter = {"user": user}
    if tags:
        filter = {"tags": tags}
    items = []
    for item in db.items.find(filter):
        item["_id"] = str(item["_id"])
        items.append(item)
    return items


@app.put("/items/{item_id}")
def update_item(item_id: str, item: Item):
    filter = {"_id": ObjectId(item_id)}
    update_item = {"$set": dict(item)}
    return {"modified_count": db.items.update_one(filter, update_item).modified_count}


@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    delete_item = {"_id": ObjectId(item_id)}
    return {"deleted_count": db.items.delete_one(delete_item).deleted_count}
