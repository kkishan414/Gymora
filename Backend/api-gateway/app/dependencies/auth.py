from app.services.auth_gateway_service import AuthGatewayService
from fastapi import Request, HTTPException

authGatewayService = AuthGatewayService()

async def verify_user(request:Request):
    response = await authGatewayService.verify_user(request)

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.json()   
        )

    return response.json()




def get_auth_gateway_service():
    return AuthGatewayService()