def cragEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "name": item["name"],
        "coordinates": item["coordinates"],
        "description": item["description"],
        "images": item["images"],
        "country": item["country"],
    }

def cragsEntity(entity) -> list:
    return [cragEntity(item) for item in entity]
