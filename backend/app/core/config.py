from pydantic import BaseSettings
from typing import List, Optional

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    CORS_ALLOWED_ORIGINS: Optional[str] = "http://localhost:3000"

    @property
    def cors_origins(self) -> List[str]:
        if not self.CORS_ALLOWED_ORIGINS:
            return []
        return [u.strip() for u in self.CORS_ALLOWED_ORIGINS.split(",")]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
