from fastapi import APIRouter,Request,Depends
from app.services.auth_gateway_service import AuthGatewayService
from fastapi.responses import JSONResponse
from app.dependencies.auth import get_auth_gateway_service,verify_user

router = APIRouter(
    prefix="/auth",
    tags = ["Authentication"]
)

@router.post("/login/")
async def login(request:Request, authGatewayService: AuthGatewayService = Depends(get_auth_gateway_service)):
    response = await authGatewayService.login(request)
    return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )

@router.post("/register/")
async def register(request:Request,authGatewayService:AuthGatewayService = Depends(get_auth_gateway_service)):
    response = await authGatewayService.register(request)
    return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )


@router.get("/verify-token")
async def verify_token(user = Depends(verify_user)):
    return user


@router.get("/refresh")
async def refresh_token(request:Request,authGatewayService:AuthGatewayService = Depends(get_auth_gateway_service)):
    response = await authGatewayService.refresh_access_token(request)
    return JSONResponse(
        status_code=response.status_code,
        content=response.json()
    )

@router.get("/logout")
async def logout(request:Request,authGatewayService:AuthGatewayService = Depends(get_auth_gateway_service)):
    response = await authGatewayService.logout(request)