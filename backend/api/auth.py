from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.database import get_db
from backend.schemas.user import RegisterRequest
from backend.services.auth_service import register_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.get("/")
def auth_home():
    return {
        "module": "Authentication",
        "status": "Ready"
    }


@router.post("/register")
def register(
    data: RegisterRequest,
    db: Session = Depends(get_db)
):
    return register_user(
        db=db,
        full_name=data.full_name,
        email=data.email,
        password=data.password
    )

