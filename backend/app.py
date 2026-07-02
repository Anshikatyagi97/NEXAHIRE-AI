from fastapi import FastAPI
from backend.api.auth import router as auth_router
from backend.api.routes import router
from backend.core.config import APP_NAME, APP_VERSION
from backend.database.database import engine
from backend.database.models import Base
from backend.models.user import User



app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="AI-powered Recruitment & Career Intelligence Platform"
)

app.include_router(router)
app.include_router(auth_router)
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": f"Welcome to {APP_NAME} 🚀"
    }