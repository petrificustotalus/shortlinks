import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    base_url: str = "http://localhost:8000"
    key_length: int = 7
    attempts: int = 2


def get_settings() -> Settings:
    settings = Settings()
    return settings
