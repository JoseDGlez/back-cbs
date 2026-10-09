from fastapi import FastAPI
from sqlalchemy import text

from app.api.routes.auth import router as auth_router
from app.api.routes.dashboard import router as dashboard_router
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import engine

app = FastAPI(
    title="CBS Distributed Application API",
    description="Backend de la solución distribuida AWS",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"],
)

app.include_router(auth_router)
app.include_router(dashboard_router)

@app.get("/")
def root():
    return {
        "message": "Backend CBS funcionando correctamente"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/health/database")
def database_health():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            result.fetchone()

        return {
            "database":"connected",
            "status":"ok"
        }
    except Exception as e:
        return {
            "database": "error",
            "status": "error",
            "message": str(e)
        }