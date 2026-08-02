from app.db.mongodb import get_database
from app.repositories.userCredentials_repository import UserCredentialsRepository
from app.repositories.refresh_session_repository import RefreshSessionRepository
from app.services.auth_service import AuthService
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from app.core.utility import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

def get_userCredentials_repository():
    db = get_database()
    return UserCredentialsRepository(db)

def get_refreshSession_repository():
    db = get_database()
    return RefreshSessionRepository(db)

def get_auth_service():
    userCredentials_repo = get_userCredentials_repository()
    refresh_repo = get_refreshSession_repository()
    return AuthService(userCredentials_repo,refresh_repo)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )
    return {
            "user_id": payload['sub'],
            "username": payload['username'],
            "email":payload['email']
            } 


