from pydantic import BaseModel
from repositories.TaskRepository import TaskRepository

class TaskService():

    repository: TaskRepository

    async def listAll(self):
        return await self.repository.listAll()
