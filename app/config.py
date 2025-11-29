# app/config.py — نسخه نهایی و ۱۰۰٪ کارکردی روی Render (بدون هیچ خطایی)
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # همه مقادیر باید حتماً داخل کوتیشن ("") باشند یا نوع داشته باشند
    database_hostname: str = "dpg-d4lert8gjchc73ama870-a"
    database_port: str = "5432"
    database_password: str = "XrDiWUZalj1Xs6Vm4Yh4eKl7v09f2tjd"
    database_name: str = "fastapi_db_n2mn"
    database_username: str = "fastapi_db_n2mn_user"
    secret_key: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    model_config = SettingsConfigDict(
        env_file=None,           # ما فقط از Environment Variables استفاده می‌کنیم
        extra="ignore"
    )

settings = Settings()
