from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.core.security import hash_password
from backend.models.user import User


def register_user(
    db: Session,
    full_name: str,
    email: str,
    password: str
):
    # Check if email already exists
    existing_user = db.query(User).filter(User.email == email).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    hashed_password = hash_password(password)

    new_user = User(
        full_name=full_name,
        email=email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id,
        "full_name": new_user.full_name,
        "email": new_user.email
    }