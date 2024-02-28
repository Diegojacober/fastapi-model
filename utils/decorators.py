from fastapi import HTTPException, status
from functools import wraps

def hasRoleKeycloak(function):
    @wraps(function)
    async def wrapper(*args, **kwargs):
        logged_user = kwargs['logged_user']
        necessary_roles: list = kwargs['roles']
        user_roles = logged_user["realm_access"]["roles"];
        for necessary_role in necessary_roles:
            if necessary_role in user_roles:    
                return await function()

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return wrapper

def hasRoleAzure(function):
    @wraps(function)
    async def wrapper(*args, **kwargs):
        logged_user = kwargs['logged_user']
        necessary_roles: list = kwargs['roles']
        user_roles = logged_user["roles"];
        for necessary_role in necessary_roles:
            if necessary_role in user_roles:    
                return await function()

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return wrapper