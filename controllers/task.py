from fastapi import APIRouter, Depends
from services.TaskService import TaskService
from config.deps import get_current_user_azure
from utils.decorators import hasRoleKeycloak, hasRoleAzure
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
async def teste(logged_user = Depends(get_current_user_azure)):
    return logged_user;


@router.get("/instrutor")
@hasRoleAzure
async def test(roles: list = ['visitor', 'instructor', 'admin'], logged_user = Depends(get_current_user_azure)):
    return 'opa';
