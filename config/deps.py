from typing import Generator, Annotated
from config.database import Session
from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError, jwt, ExpiredSignatureError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import status, HTTPException, Depends
from pydantic import BaseModel
from infra.keycloak import keycloak_openid


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_session() -> Generator:
    session: AsyncSession = Session()
    
    try:
        yield session
    finally:
        await session.close()
        
async def get_current_user(token: str):
    """
    :param token: jwt token
    :return:
    """
    decoded_data = jwt.decode(jwt=token, key='secret', algorithms=[ALGORITHM])

    return decoded_data



class TokenData(BaseModel):
    username: str | None = None

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        KEYCLOAK_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\n" + keycloak_openid.public_key() + "\n-----END PUBLIC KEY-----"
        options = {"verify_signature": True, "verify_aud": False, "verify_exp": True}
        token_info = keycloak_openid.decode_token(token, key=KEYCLOAK_PUBLIC_KEY, options=options)
    except ExpiredSignatureError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Expired Token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except JWTError as e:
        raise credentials_exception
    return token_info