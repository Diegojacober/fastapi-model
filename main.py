from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from config.routers import configure_routers


def create_application():
    application = FastAPI()

    configure_routers(application)

    return application

core_module = create_application()

