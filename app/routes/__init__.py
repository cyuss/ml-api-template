from fastapi import APIRouter

from app.routes import sample_route

api_router = APIRouter()

api_router.include_router(sample_route.router)