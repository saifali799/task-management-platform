from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.schemas.user import UserCreate, Token, UserOut
from app.services.user_service import register_user
from app.services.auth_service import authenticate_user, create_token_for_user

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    try:
        user = register_user(db, payload)
        return user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/token", response_model=Token)
def login(form_data: UserCreate, db: Session = Depends(get_db)):
    user_id = authenticate_user(db, form_data.email, form_data.password)
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    token = create_token_for_user(user_id)
    return {"access_token": token, "token_type": "bearer"}
