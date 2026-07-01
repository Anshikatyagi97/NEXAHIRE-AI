from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status": "healthy",
        "project": "NEXAHIRE-AI",
        "version": "1.0.0"
    }

@router.get("/about")
def about():
    return {
        "project": "NEXAHIRE-AI",
        "description": "AI-powered Recruitment & Career Intelligence Platform",
        "status": "Development"
    }