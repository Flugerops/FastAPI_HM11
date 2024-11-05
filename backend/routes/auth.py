from typing import Annotated

from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session


from ..utils import get_current_user, hash_pwd
from ..db import User, AsyncDB


auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get(
    "/users/me",
    summary="Get current user",
    description="Get current user by oauth2 token",
    response_description="Current User",
)
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return {"current_user": current_user}


@auth_router.post(
    "/token",
    summary="Token url for oauth2",
    description="Select user in db and return access token and token type",
    response_description="Access token and token type in json",
)
async def login(
    form: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[Session, Depends(AsyncDB.get_session)],
):
    """
    Finds user and return access token
    OAuth2PasswordRequestForm
    - **username**: user`s username
    - **password**: user`s password(not hashed!!)
    - **client_id**: optional
    - **client_secret**: optional
    """
    print(form.username)
    user = session.scalar(select(User).where(User.username == form.username))
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    hashed_password = hash_pwd(form.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=402, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}
