from pydantic import BaseModel

class Route(BaseModel):
    _id: str
    name: str
    grade: str
    author: str
    cragId: str
    sectorId: str
    type: str
