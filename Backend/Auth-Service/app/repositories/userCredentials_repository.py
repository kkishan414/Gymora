from app.models.user_credentials import UserCredentials
from app.core.constants import Const

class UserCredentialsRepository:

    def __init__(self,db):
        self.db = db
        self.collection = self.db[Const.USER_CREDENTIALS_COLLECTION]

    async def get_user_by_email(self, email:str):
        return await self.collection.find_one({"email":email})
    
    async def get_user_by_username(self, username:str):
        return await self.collection.find_one({"username":username})

    async def add_user_in_userCredentails(self,userCredential: UserCredentials):
        try:
            await self.collection.insert_one(userCredential.model_dump())
        except Exception:
            raise

    async def get_user_by_email_or_username(self, user:str):
        return await self.collection.find_one(
            {
                "$or": [
                    {"email": user},
                    {"username": user}
                ]
            }
        )
