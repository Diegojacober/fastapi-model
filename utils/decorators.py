from fastapi import HTTPException, status
from functools import wraps

def isInstructor(function):
    @wraps(function)
    async def wrapper(*args, **kwargs):
        logged_user = kwargs['logged_user']
        roles = logged_user["realm_access"]["roles"];
        if ("instructor" in roles):
            return await function()
        
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    return wrapper
