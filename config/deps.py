from typing import Generator
from config.database import Session
from sqlalchemy.ext.asyncio import AsyncSession

async def get_session() -> Generator:
    session: AsyncSession = Session()
    
    try:
        yield session
    finally:
        await session.close()