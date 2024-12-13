from fastapi import FastAPI
from routes.crag import crag
from routes.festivals import festival
from routes.sectors import sector
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


origins = [
    "http://localhost:3000",
    "https://kosciukiewicz-adam.github.io/topo/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

routers = crag, sector, festival

for router in routers:
    app.include_router(router)
