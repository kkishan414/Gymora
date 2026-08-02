from pydantic import BaseModel
from datetime import datetime
from app.models.enums import FitnessGoal, ActivityLevel, ExperienceLevel
from typing import Optional

class FitnessProfile(BaseModel):
    user_id: str 
    current_weight: float 
    goal: FitnessGoal
    activity_level: ActivityLevel
    experience_level: ExperienceLevel
    target_weight: Optional[float] = None
    body_fat: Optional[float] = None
    created_at: datetime 
    updated_at: datetime 
    