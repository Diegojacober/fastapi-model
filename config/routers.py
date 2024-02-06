from fastapi import FastAPI
from controllers import task as task_router

def configure_routers(application: FastAPI):
    application.include_router(task_router.router)