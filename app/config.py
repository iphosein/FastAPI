# app/config.py — بهترین و تمیزترین روش (مثل Netflix, Instagram)
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str          # فقط یک متغیر!
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    model_config = SettingsConfigDict(env_file=None)

settings = Settings()
