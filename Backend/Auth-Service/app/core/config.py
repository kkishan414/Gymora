from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    APP_ENV: str
    CONNECTION_STRING: str
    DATABASE: str
    JWT_SECRET: str
    JWT_ALGORITHM: str

    model_config = SettingsConfigDict(
    env_file = ".env",
    env_file_encoding="utf-8"
    )

settings = Settings()