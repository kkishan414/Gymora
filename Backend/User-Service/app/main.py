from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db import mongodb
from app.api import userAPI

# -> defining lifespan of application (Creating connection when app starts/ closing connection when app shutsdown)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await mongodb.connect_to_mongo()
    yield 
    mongodb.close_connection()

app = FastAPI(lifespan=lifespan)


app.include_router(userAPI.router)