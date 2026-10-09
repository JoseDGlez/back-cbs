from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import create_access_token
from app.db.database import get_db
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth_service import login_user

router = APIRouter(
    prefix="/api",
    tags=["Authentication"]
)

@router.post(
    "/login",
    response_model=TokenResponse
)

def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db)
):
    token = login_user(
        db,
        credentials.username,
        credentials.password
    )

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
