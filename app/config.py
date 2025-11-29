from pydantic_settings import BaseSettings, SettingsConfigDict

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    database_hostname: dpg-d4lert8gjchc73ama870-a
    database_port: 5432
    database_password: XrDiWUZalj1Xs6Vm4Yh4eKl7v09f2tjd
    database_name: fastapi_db_n2mn
    database_username: fastapi_db_n2mn_user
    secret_key: "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    algorithm: HS256
    access_token_expire_minutes: 30

    # model_config = SettingsConfigDict(env_file="../.env")
    """model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )"""
settings = Settings()


