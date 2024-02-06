from sqlalchemy.ext.declarative import declarative_base


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# import os
# from dotenv import load_dotenv

from pydantic import BaseModel

from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseModel):
    
    API_V1_STR: str = '/api/v1'
    DB_URL: str = f"postgresql+asyncpg://devuser:changeme@localhost:5433/devdb"
    # DB_URL: str = f"mysql+asyncmy://{__USER}:{__PASS}@{__HOST}/{__DATABASE}"
    DB_BASEMODEL: any = declarative_base()
    
    class Config:
        arbitrary_types_allowed=True
        case_sensitive = True
        from_attributes = True
    
settings = Settings()