from datetime import timedelta
from typing import Optional
from app.repositories.user_repo import get_user_by_email
from app.services.security import verify_password, create_access_token

def authenticate_user(db, email: str, password: str) -> Optional[int]:
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user.id

def create_token_for_user(user_id: int):
    access_token_expires = timedelta(minutes=60)
    token = create_access_token(subject=str(user_id), expires_delta=access_token_expires)
    return token
