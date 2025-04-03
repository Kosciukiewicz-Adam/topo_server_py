from fastapi import APIRouter
from config.db import connection
from schemas.route import routesEntity
from schemas.sector import sectorEntity, sectorsEntity
from bson.objectid import ObjectId

sector = APIRouter()

@sector.get("/sectors")
async def get_all_sectors():
    sectors = sectorsEntity(connection.test.sectors.find())
    return sectors

@sector.get("/sectors/{sectorId}")
async def get_sector(sectorId):
    sector =  sectorEntity(connection.test.sectors.find_one({"_id": ObjectId(sectorId)}))
    sector["routesAmount"] = await get_routes_amount(sectorId)
    return sector

@sector.get("/sectors/{cragId}/routes")
async def get_sector_routes(cragId):
    return routesEntity(connection.test.routes.find({"sectorId": ObjectId(cragId)}))

async def get_routes_amount(sectorId):
    return len(await get_sector_routes(sectorId))