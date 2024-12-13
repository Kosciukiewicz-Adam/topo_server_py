def sectorEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "name": item["name"],
        "image": item["image"],
        "imageWithRoutes": item["imageWithRoutes"],
        "cragId": str(item["cragId"]),
    }

def sectorsEntity(entity) -> list:
    return [sectorEntity(item) for item in entity]
