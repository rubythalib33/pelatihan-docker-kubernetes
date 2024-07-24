# app/crud.py
from models import MongoDB, to_dict
from schemas import TodoItem
from bson import ObjectId

class TodoCRUD:
    def __init__(self, db: MongoDB):
        self.collection = db.db['todos']

    async def create_todo_item(self, item: TodoItem):
        result = await self.collection.insert_one(item.dict())
        return await self.get_todo_item(result.inserted_id)

    async def get_todo_item(self, item_id: str):
        item = await self.collection.find_one({"id": item_id})
        return to_dict(item) if item else None

    async def get_all_todo_items(self):
        items = self.collection.find()
        return [to_dict(item) async for item in items]

    async def update_todo_item(self, item_id: str, item: TodoItem):
        await self.collection.update_one({"id": item_id}, {"$set": item.dict()})
        return await self.get_todo_item(item_id)

    async def delete_todo_item(self, item_id: str):
        await self.collection.delete_one({"id": item_id})
