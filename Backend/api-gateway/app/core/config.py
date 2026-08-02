from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    GATEWAY_HOST:str 
    GATEWAY_PORT:int
    AUTH_SERVICE_URL:str
    USER_SERVICE_URL:str 

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()

