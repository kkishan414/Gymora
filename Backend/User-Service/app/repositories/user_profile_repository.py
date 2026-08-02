from app.models.user_profile import UserProfile
from app.core.constants import Const

class UserProfileRepository:
    def __init__(self,db):
        self.db = db 
        self.collection = self.db[Const.USER_PROFILE_COLLECTION]

    async def create_user_profile(self, userProfile:UserProfile):
        await self.collection.insert_one(userProfile.model_dump())
        
    
    async def get_user_profile_by_user_id(self, user_id:str):
        return await self.collection.find_one({"user_id":user_id})
    
