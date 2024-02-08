from fastapi import APIRouter, Depends
from services.TaskService import TaskService
from config.deps import get_current_user
from utils.decorators import hasRole
from sqlalchemy.ext.asyncio import AsyncSession
from config.deps import get_session


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"description": "Not found"}},
)



@router.get("/",)
async def list_all( db: AsyncSession = Depends(get_session)):
    service = TaskService(db)
    return await service.listAll()

@router.get("/teste",)
async def teste(logged_user = Depends(get_current_user)):
    return logged_user;


@router.get("/instrutor")
@hasRole
async def test(roles: list = ['visitor', 'instructor'], logged_user = Depends(get_current_user)):
    return 'opa';
