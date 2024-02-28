from domain.entities.Task import Task
from domain.entities.Task import TaskStatus
from config.deps import get_session
from sqlalchemy.future import select
from typing import List

class TaskRepository():

    def __init__(self, db):
        self.model: Task
        self.db = db
    
    async def listAll(self):
        async with self.db as session:
            query = select(Task)
            result = await session.execute(query)
            results: List[Task] = result.scalars().unique().all()
            return results
