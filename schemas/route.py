def routeEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "cragId": str(item["cragId"]),
        "sectorId" :str(item["sectorId"]),
        "name": item["name"],
        "grade": item["grade"],
        "author": item["author"],
        "type": item["type"],
    }

def routesEntity(entity) -> list:
    return [routeEntity(item) for item in entity]
