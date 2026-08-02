from app.core.constants import Const
from app.core.config import settings
from motor.motor_asyncio import AsyncIOMotorClient
import logging


client = None
db = None


async def connect_to_mongo():
    try:
        global client,db
        client = AsyncIOMotorClient(settings.CONNECTION_STRING)
        await client.admin.command('ping')
        logging.info("Successfully connected to MongoDB Atlas!")
        db = client.get_database(settings.DATABASE)
        userCredentials_collection = db[Const.USER_CREDENTIALS_COLLECTION]

        await userCredentials_collection.create_index("email",unique = True)
        await userCredentials_collection.create_index("username",unique= True)
        await userCredentials_collection.create_index("user_id", unique= True)

        
    except Exception as e:
        logging.error(f"Failed to connect to mongodb: {e}")
        raise 



def get_database():
    if db is None:
        raise RuntimeError("Database not initialized. Connect to mongo first!!")
    return db

def close_connection():
    global client, db
    if client:
        client.close()
        logging.info("MongoDB connection closed.")
        client = None
        db = None