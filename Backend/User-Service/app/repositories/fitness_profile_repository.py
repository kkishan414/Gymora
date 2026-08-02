from app.models.fitness_profile import FitnessProfile
from app.core.constants import Const

class FitnessProfileRepository:
    def __init__(self,db):
        self.db = db 
        self.collection = self.db[Const.FITNESS_PROFILE_COLLECTION]

    async def create_fitness_profile(self,fitnessProfile: FitnessProfile):
        await self.collection.insert_one(fitnessProfile.model_dump())
        
    async def get_fitness_profile_by_user_id(self, user_id:str):
        return await self.collection.find_one({"user_id":user_id})