def festivalEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "name": item["name"],
        "cragId": str(item["cragId"]),
        "country": item["country"],
        "date": item["date"],
        "description": item["description"],
        "images": item["images"],
        "website": item["website"],
        "location": item["location"],
    }

def festivalsEntity(entity) -> list:
    return [festivalEntity(item) for item in entity]
