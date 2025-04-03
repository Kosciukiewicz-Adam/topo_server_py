def statsEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "date": item["date"],
        "ip": item["ip"],
        "location": item["location"]
    }

def statsEntity(entity) -> list:
    return [statsEntity(item) for item in entity]
