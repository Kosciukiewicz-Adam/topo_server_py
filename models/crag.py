from pydantic import BaseModel

class Crag(BaseModel):
    _id: str
    name: str
    coordinates: list[str]
    images: list[str]
    description: str
    country: str
    routesAmount: int
