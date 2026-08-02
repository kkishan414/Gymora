from fastapi import APIRouter,Request,Depends
from app.dependencies import get_auth_gateway_service
from app.services.auth_gateway_service import AuthGatewayService


router = APIRouter(
    prefix="/auth",
    tags = ["Authentication"]
)

@router.post("/login/")
async def login(request:Request, authGatewayService: AuthGatewayService = Depends(get_auth_gateway_service)):
    return await authGatewayService.login(request)

@router.post("/register/")
async def register(request:Request,authGatewayService:AuthGatewayService = Depends(get_auth_gateway_service)):
    return await authGatewayService.register(request)

@router.get("/verify-token")
async def verify_token(request:Request, authGatewayService:AuthGatewayService = Depends(get_auth_gateway_service)):
    return await authGatewayService.verify_user(request)