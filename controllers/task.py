from fastapi import APIRouter, Depends
from services.TaskService import TaskService
from config.deps import get_current_user
from utils.decorators import isInstructor


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"description": "Not found"}},
)

service = TaskService()

@router.get("/",)
async def list_all():
    return await service.listAll()

@router.get("/teste",)
async def teste(logged_user = Depends(get_current_user)):
    return logged_user;


@router.get("/instrutor")
@isInstructor
async def test(logged_user = Depends(get_current_user)):
    return "teste";
