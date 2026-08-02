from fastapi import APIRouter,Depends
from app.schemas.create_profile_request import CreateProfileRequest
from app.services.user_service import UserService
from app.dependencies import get_user_service


router = APIRouter(
    prefix="/profile",
    tags=['profile']
)



@router.post("/onboarding")
async def onboarding(create_profile: CreateProfileRequest, user_service: UserService = Depends(get_user_service)):
    pass