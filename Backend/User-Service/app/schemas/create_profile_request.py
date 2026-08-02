from pydantic import BaseModel
from datetime import date
from typing import Optional
from app.models.enums import(Gender,FitnessGoal,ActivityLevel,ExperienceLevel)

class CreateProfileRequest(BaseModel):
    # user profile 
    name: str 
    bio: Optional[str] = None
    gender: Gender
    dob: date
    height: float 

    # fitness profile 
    current_weight: float 
    goal: FitnessGoal
    activity_level: ActivityLevel
    experience_level: ExperienceLevel
    target_weight: Optional[float] = None
    body_fat: Optional[float] = None