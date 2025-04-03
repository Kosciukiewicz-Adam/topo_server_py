from fastapi import APIRouter
from config.db import connection
from schemas.crag import cragsEntity, cragEntity
from schemas.route import routesEntity
from schemas.sector import sectorsEntity
from bson.objectid import ObjectId

crag = APIRouter()

@crag.get("/crags")
async def get_all_crags():
    cragsList = cragsEntity(connection.test.crags.find())

    for crag in cragsList:
        crag["routesAmount"] = await get_routes_amount(crag["_id"])

    return cragsList

@crag.get("/crags/{cragId}")
async def get_crag(cragId):
    crag =  cragEntity(connection.test.crags.find_one({"_id": ObjectId(cragId)}))
    crag["routesAmount"] = await get_routes_amount(cragId)
    return crag

@crag.get("/crags/{cragId}/routes")
async def get_crag_routes(cragId):
    return routesEntity(connection.test.routes.find({"cragId": ObjectId(cragId)}))

@crag.get("/crags/{cragId}/sectors")
async def get_crag_sectors(cragId):
    return sectorsEntity(connection.test.sectors.find({"cragId": ObjectId(cragId)}))

async def get_routes_amount(cragId):
    all_routes = await get_crag_routes(cragId)
    return len(all_routes)