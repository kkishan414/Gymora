from pydantic import BaseModel
from datetime import datetime,date
from app.models.enums import Gender
from typing import Optional

class UserProfile(BaseModel):
    user_id: str 
    username: str 
    email: str 
    name: str 
    bio: Optional[str] = None
    gender: Gender
    dob: date
    height: float 
    created_at: datetime 
    updated_at: datetime 



