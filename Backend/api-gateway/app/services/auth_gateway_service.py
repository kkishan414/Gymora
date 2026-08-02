from fastapi import Request
from fastapi.responses import JSONResponse
import httpx
from app.core.config import settings

class AuthGatewayService:
    async def login(self, request: Request):
        data = await request.json()
        url = f"{settings.AUTH_SERVICE_URL}/auth/login/"
        async with httpx.AsyncClient() as client:
            response = await client.post(url,json=data)
        return JSONResponse(
            status_code=response.status_code,
            content = response.json() 
        )

    async def register(self,request:Request):
        data = await request.json() 
        url = f"{settings.AUTH_SERVICE_URL}/auth/register/"
        async with httpx.AsyncClient() as client:
            response = await client.post(url,json=data)
        return JSONResponse(
            status_code=response.status_code,
            content= response.json() 
        )
    
    async def verify_user(self,request:Request):
        url = f"{settings.AUTH_SERVICE_URL}/auth/verify-token"
        headers = {
            "Authorization":request.headers.get("Authorization")
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(url,headers=headers)
        return JSONResponse(
            status_code= response.status_code,
            content=response.json()
            )
    
