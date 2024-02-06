from fastapi import APIRouter
from services.TaskService import TaskService

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},

)

service = TaskService()

@router.get("/",)
async def list_all():
    return await service.listAll()