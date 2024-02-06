from typing import Optional
from domain.enums.TaskStatus import TaskStatus

from pydantic import BaseModel

class TaskSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str]
    status: Optional[TaskStatus]
    
    class Config:
        from_attributes = True
