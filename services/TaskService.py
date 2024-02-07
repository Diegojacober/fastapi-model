from fastapi import Depends
from config.deps import get_session
from repositories.TaskRepository import TaskRepository

class TaskService():

    def __init__(self, db: Depends(get_session)):
        self.repository = TaskRepository(db)

    async def listAll(self):
        return await self.repository.listAll()
