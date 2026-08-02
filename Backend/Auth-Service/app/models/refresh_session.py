from pydantic import BaseModel
from datetime import datetime

class RefreshSession(BaseModel):
    user_id:str
    username:str
    email:str
    token_hash:str
    created_at:datetime
    expires_at:datetime
    is_revoked: bool = False
