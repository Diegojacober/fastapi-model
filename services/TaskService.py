from repositories.TaskRepository import TaskRepository

class TaskService():

    def __init__(self, db):
        self.repository = TaskRepository(db)

    async def listAll(self):
        return await self.repository.listAll()
