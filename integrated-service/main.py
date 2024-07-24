# app/main.py
from typing import List
from fastapi import FastAPI, HTTPException
from models import MongoDB
from crud import TodoCRUD
from schemas import TodoItem
from motor.motor_asyncio import AsyncIOMotorClient
import os

mongo_host = os.getenv('MONGO_HOST', 'localhost')
app = FastAPI()
db = MongoDB(uri=f"mongodb://{mongo_host}:27017", db_name="tododb")
crud = TodoCRUD(db=db)

@app.post("/todos/", response_model=TodoItem)
async def create_todo_item(item: TodoItem):
    return await crud.create_todo_item(item)

@app.get("/todos/{item_id}", response_model=TodoItem)
async def read_todo_item(item_id: str):
    item = await crud.get_todo_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.get("/todos/", response_model=List[TodoItem])
async def read_all_todo_items():
    return await crud.get_all_todo_items()

@app.put("/todos/{item_id}", response_model=TodoItem)
async def update_todo_item(item_id: str, item: TodoItem):
    updated_item = await crud.update_todo_item(item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@app.delete("/todos/{item_id}")
async def delete_todo_item(item_id: str):
    await crud.delete_todo_item(item_id)
    return {"detail": "Item deleted"}
