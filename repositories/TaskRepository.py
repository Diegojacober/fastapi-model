from domain.entities.Task import Task
from domain.entities.Task import Task, TaskStatus
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.deps import get_session
from sqlalchemy.future import select
from typing import List

class TaskRepository():

    def __init__(self, db: AsyncSession):
        self.model: Task = Task
        self.db: AsyncSession = db
    
    async def listAll(self):
        async with self.db as session:
            query = select(self.model)
            result = await session.execute(query)
            results: List[self.model] = result.scalars().unique().all()
            return results
