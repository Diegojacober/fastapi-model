from pydantic import Field
from ..enums.TaskStatus import TaskStatus
from sqlalchemy import Column, Integer, String
from infra.database import settings

class Task(settings.DB_BASEMODEL):
    __tablename__ = 'tasks'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str =  Column(String(256))
    status: TaskStatus = Column(String(256),default=TaskStatus.DRAFT)