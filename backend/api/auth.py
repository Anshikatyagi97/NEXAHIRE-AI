

from fastapi import APIRouter

from backend.schemas.user import RegisterRequest
from backend.services.auth_service import register_user




router = APIRouter(prefix="/auth", tags=["Authentication"])



@router.get("/")
def auth_home():
    return {
        "module": "Authentication",
        "status": "Ready"
    }

@router.post("/register")
def register(data: RegisterRequest):
    return register_user(
        full_name=data.full_name,
        email=data.email
    )