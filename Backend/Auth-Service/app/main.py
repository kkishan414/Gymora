from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db import mongodb
from app.api import auth


# -> defining lifespan of application (creating connection when app starts/ closing connection when app shutsdown)
@asynccontextmanager
async def lifespan(app: FastAPI):
    await mongodb.connect_to_mongo()
    yield
    mongodb.close_connection()

# Creating fastapi app
app = FastAPI(lifespan=lifespan)


# adding Dependency injection for auth router
app.include_router(auth.router)











