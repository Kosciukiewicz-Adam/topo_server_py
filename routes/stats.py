from fastapi import APIRouter
from config.db import connection
from schemas.stats import statsEntity
from pydantic import BaseModel

class Item(BaseModel):
    ip: str
    location: str
    date: str

stats = APIRouter()

@stats.post("/stats")
async def saveStat(item: Item):
    existing_entry = connection.test.stats.find_one({"ip": item.ip, "location": item.location})

    if existing_entry:
        connection.test.stats.update_one(
            {"_id": existing_entry["_id"]},
            {"$push": {"date": item.date}}
        )
    else:
        connection.test.stats.insert_one({
            "ip": item.ip,
            "location": item.location,
            "date": [item.date]
        })

    return {"message": "Stat saved successfully"}
