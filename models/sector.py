from pydantic import BaseModel

class Sector(BaseModel):
    _id: str
    name: str
    image: str
    imageWithRoutes: str
    cragId: str
    routesAmount: int