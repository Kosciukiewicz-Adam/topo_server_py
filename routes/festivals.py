from fastapi import APIRouter
from config.db import connection
from schemas.festival import festivalsEntity
from bson.objectid import ObjectId

festival = APIRouter()

@festival.get("/festivals")
async def get_all_festivals():
    return festivalsEntity(connection.test.festivals.find())
