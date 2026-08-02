from fastapi import FastAPI
from app.api import auth

app = FastAPI(
    title="Gymora API Gateway",
    version = "1.0.1"
)

app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message":"api gateway is running"}