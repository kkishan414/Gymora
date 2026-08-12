import uuid
from passlib.context import CryptContext
from datetime import timedelta,datetime,timezone
from app.core.config import settings
from jose import jwt,JWTError
import secrets
import hashlib

def generate_user_id():
    return f"USR_{uuid.uuid4().hex[:12]}"

def create_hash_password(password: str):
    bcrpyt_context = CryptContext(schemes=['bcrypt'],deprecated = 'auto')
    return bcrpyt_context.hash(password)

def verify_password(password: str,hash_password:str):
    bcrpyt_context = CryptContext(schemes=['bcrypt'],deprecated = 'auto')
    if bcrpyt_context.verify(password,hash_password):
        return True 
    else: 
        return False
    
def create_access_token(username:str, user_id:str,email:str,expires_delta:timedelta ):
    SECRET_KEY = settings.JWT_SECRET
    ALGORITM = settings.JWT_ALGORITHM
    encode = {'sub':user_id,'username':username,'email':email}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITM)

def decode_access_token(token:str):
    SECRET_KEY = settings.JWT_SECRET
    ALGORITM = settings.JWT_ALGORITHM
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITM]
        )
        return payload
    except JWTError:
        return None
    
def create_refresh_token():
    return secrets.token_urlsafe(64)

def hash_refresh_token(token:str):
    return hashlib.sha256(token.encode()).hexdigest()

