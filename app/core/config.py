from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Chat API"
    env: str = "dev"  # dev|staging|prod
    api_prefix: str = "/api"
    version: str = "0.1.0"

    jwt_secret: str = "CHANGE_ME"
    jwt_algorithm: str = "HS256"
    jwt_access_minutes: int = 30
    jwt_refresh_days: int = 7

    database_url: str = "postgresql+asyncpg://postgres:development@localhost:5432/chat_db"

    enable_prometheus: bool = False

    model_config = SettingsConfigDict(env_file=".env", env_prefix="APP_")


settings = Settings()
