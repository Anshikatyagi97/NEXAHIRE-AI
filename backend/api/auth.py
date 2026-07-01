from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.get("/")
def auth_home():
    return {
        "module": "Authentication",
        "status": "Ready"
    }