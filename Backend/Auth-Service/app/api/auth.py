from fastapi import APIRouter,Depends
from app.dependencies import get_auth_service, get_current_user
from app.schemas.register_request import RegisterRequest
from app.schemas.refresh_token_request import RefreshTokenRequest
from app.services.auth_service import AuthService
from app.models.user_credentials import Token
from typing import Annotated
from app.schemas.login_request import LoginRequest
from app.schemas.logout_request import LogoutRequest

router = APIRouter(
    prefix="/auth",
    tags=['auth']
)



@router.post("/register/")
async def register(request: RegisterRequest,auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.register(
        request.username,
        request.email,
        request.password,
        request.confirm_password
    )

@router.post("/login/")
async def login_for_access_token(request:LoginRequest,auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.login(request.username,request.password)



@router.get("/me")
async def get_me(user = Depends(get_current_user)):
    return user

@router.get("/verify-token")
async def verify_token(current_user = Depends(get_current_user)):
    return current_user


@router.post("/refresh")
async def refresh_session(request: RefreshTokenRequest,auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.refresh_access_token(request.refresh_token)


@router.post("/logout")
async def logout(request: LogoutRequest,auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.logout_user(request.refresh_token)