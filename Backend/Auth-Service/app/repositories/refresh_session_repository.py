

class RefreshSessionRepository:
    
    def __init__(self,db):
        self.collection = db["refresh_sessions"]

    async def create_session(self,session):
        await self.collection.insert_one(session.model_dump())

    async def get_session_by_hash(self,token_hash):
        return await self.collection.find_one({
            "token_hash":token_hash
        })
    
    async def revoke_session(self, token_hash):
        await self.collection.update_one(
            {"token_hash": token_hash},
            {"$set": {"is_revoked": True}}
        )