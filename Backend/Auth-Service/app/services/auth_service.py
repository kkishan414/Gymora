from app.repositories.userCredentials_repository import UserCredentialsRepository
from app.repositories.refresh_session_repository import RefreshSessionRepository
from app.db.mongodb import get_database
from app.models.user_credentials import UserCredentials
from app.models.refresh_session import RefreshSession
from app.core import utility
from datetime import datetime,timedelta
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException
from datetime import datetime,UTC

class AuthService:

    def __init__(self,userCredentials_repo: UserCredentialsRepository,refreshSession_repo:RefreshSessionRepository):
        self.userCredential_repo = userCredentials_repo
        self.refresh_repo = refreshSession_repo

    async def login(self, user:str, password:str):
        #check if it is username or email
        db_user = await self.userCredential_repo.get_user_by_email_or_username(user)
        
        if db_user:
            if utility.verify_password(password, db_user['hash_password']):
                access_token = utility.create_access_token(db_user["username"],db_user["user_id"],db_user["email"],timedelta(minutes=20))
                refresh_token = utility.create_refresh_token()
                refresh_token_hash = utility.hash_refresh_token(refresh_token)
                print(refresh_token_hash)
                session = RefreshSession(
                    user_id= db_user["user_id"],
                    username=db_user["username"],
                    email=db_user["email"],
                    token_hash=refresh_token_hash,
                    created_at=datetime.now(UTC),
                    expires_at=datetime.now(UTC) + timedelta(days=90)
                )
                await self.refresh_repo.create_session(session)

                return {'access_token':access_token,'refresh_token':refresh_token,'token_type':'bearer'}
            else:
                raise HTTPException(
                    status_code=400,
                    detail="username/password is incorrect!!"
                )
        
        raise HTTPException(
            status_code=400,
            detail="username/password is incorrect!!"
        )


    async def register(self, username:str, email: str, password: str, confirm_password: str):
        #check if username and email already exists
        existing_email = await self.userCredential_repo.get_user_by_email(email)
        if existing_email:
            raise HTTPException(
                status_code=400,
                detail="email already exists!!"
            )
        
        existing_username = await self.userCredential_repo.get_user_by_username(username)
        if existing_username:
            raise HTTPException(
                status_code=400,
                detail="username already exists!!"
            )


        userCredential = UserCredentials(
        user_id = utility.generate_user_id(),
        username = username,
        email = email ,
        hash_password = utility.create_hash_password(password),
        is_active = True,
        created_at = datetime.now(UTC),
        updated_at = datetime.now(UTC)
        )
        print(userCredential.user_id)
        try: 
            await self.userCredential_repo.add_user_in_userCredentails(userCredential)
        except DuplicateKeyError:
            raise HTTPException(
                status_code=400,
                detail="Duplicate record found"
            )
    
        
    async def refresh_access_token(self,refresh_token:str):
        hash_token = utility.hash_refresh_token(refresh_token)
        print(hash_token)
        session = await self.refresh_repo.get_session_by_hash(hash_token)
        if not session:
            raise HTTPException(
                status_code=401,
                detail="Invalid Refresh Token"
            )
        elif (session["is_revoked"] == True):
            raise HTTPException(
                status_code=401,
                detail="Refresh token expired"
            )
        elif ( (datetime.now(UTC) >= session["expires_at"].replace(tzinfo=UTC)) ):
            await self.refresh_repo.revoke_session(hash_token)
            raise HTTPException(
                status_code=401,
                detail="Refresh token expired"
            )
        else:
            access_token = utility.create_access_token(session["username"],session["user_id"],session["email"],timedelta(minutes=20))
            return {
                "access_token":access_token,
                "refresh_token":refresh_token,
                "token_type":"bearer"
            }

    async def logout_user(self,refresh_token:str):
        hash_token = utility.hash_refresh_token(refresh_token)
        session = await self.refresh_repo.get_session_by_hash(hash_token)
        if not session:
            raise HTTPException(
                status_code=401,
                detail="Invalid Refresh Token"
            )
        await self.refresh_repo.revoke_session(hash_token)
        
            