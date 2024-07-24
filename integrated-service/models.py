# app/models.py
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

class MongoDB:
    def __init__(self, uri: str, db_name: str):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[db_name]

def to_dict(obj) -> dict:
    return {k: str(v) if isinstance(v, ObjectId) else v for k, v in obj.items()}
