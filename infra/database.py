from sqlalchemy.ext.declarative import declarative_base

from pydantic import BaseModel

from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseModel):
    
    API_V1_STR: str = '/api/v1'
    DB_URL: str = f"postgresql+asyncpg://devuser:changeme@localhost:5433/devdb"
    # DB_URL: str = f"mysql+asyncmy://{__USER}:{__PASS}@{__HOST}/{__DATABASE}"
    DB_BASEMODEL: any = declarative_base()
    
    class Config:
        arbitrary_types_allowed=True
    
settings = Settings()