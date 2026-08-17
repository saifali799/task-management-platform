from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user_repo import get_user_by_email, create_user, get_user
from app.services.security import hash_password
from app.schemas.user import UserCreate

def register_user(db: Session, payload: UserCreate) -> User:
    existing = get_user_by_email(db, payload.email)
    if existing:
        raise ValueError("Email already registered")
    user = User(email=payload.email, full_name=payload.full_name, hashed_password=hash_password(payload.password))
    return create_user(db, user)

def get_user_profile(db: Session, user_id: int) -> User:
    user = get_user(db, user_id)
    if not user:
        raise ValueError("User not found")
    return user
