from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from app.api.routes import auth, users, tasks
from app.core.config import settings
from app.api.exceptions import register_exception_handlers

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)

def create_app() -> FastAPI:
    app = FastAPI(title="Task Management API")

    origins = settings.cors_origins
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
    app.include_router(users.router, prefix="/api/users", tags=["users"])
    app.include_router(tasks.router, prefix="/api/tasks", tags=["tasks"])

    @app.get("/health", tags=["health"])
    def health():
        return {"status": "ok"}

    register_exception_handlers(app)

    return app

app = create_app()
