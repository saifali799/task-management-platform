from fastapi import APIRouter, Depends
from app.api.dependencies import get_current_user
from app.schemas.user import UserOut

router = APIRouter()

@router.get("/me", response_model=UserOut)
def read_profile(current_user = Depends(get_current_user)):
    return current_user
