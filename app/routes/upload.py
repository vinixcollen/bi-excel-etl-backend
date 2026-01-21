from fastapi import APIRouter
from app.handlers.upload import get_all_uploads_handler

router = APIRouter(
    prefix="/uploads",
)

@router.get('/')
async def get_uploads():
    return await get_all_uploads_handler()

@router.post('/')
async def create_upload():
    pass