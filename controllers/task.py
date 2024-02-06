from fastapi import APIRouter, Depends
from services.TaskService import TaskService
from config.deps import get_current_user

from typing import Annotated

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)

service = TaskService()

@router.get("/",)
async def list_all():
    return await service.listAll()

@router.get("/teste",)
async def teste(logged_user = Depends(get_current_user)):
    return logged_user;