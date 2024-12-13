from pydantic import BaseModel

class Festival(BaseModel):
    _id: str
    name: str
    cragId: str
    country: str
    date: str
    description: str
    images: list[str]
    website: str
    location: str

