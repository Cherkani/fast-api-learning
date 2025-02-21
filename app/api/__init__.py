from fastapi import APIRouter
from ..controllers import developer_controller

api_router = APIRouter()

api_router.include_router(
    developer_controller.router,
    prefix="/api",
    tags=["developers"]
)
