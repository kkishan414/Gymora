from pydantic import BaseModel
from datetime import datetime

class UserCredentials(BaseModel):
    user_id: str
    username: str
    email: str
    hash_password: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
    
class Token(BaseModel):
    access_token:str
    token_type:str


