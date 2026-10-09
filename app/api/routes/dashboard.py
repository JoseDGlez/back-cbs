from fastapi import APIRouter, Depends

from app.core.security import get_current_username

router = APIRouter(
    prefix="/api",
    tags=["Dashboard"]
)

@router.get("/dashboard")
def dashboard(
    username: str = Depends(get_current_username)
):
    return {
    "message": "Acceso autorizado al Dashboard",
    "username": username,
    "authenticated": True
    }
