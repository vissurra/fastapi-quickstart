import datetime
from typing import Annotated

from fastapi import Header

from app.database.user import User, UserToken
from app.exception.auth import AuthException
from app.tool import jwt_tools


def get_current_user(token: Annotated[str, Header()]) -> User:
    payload = jwt_tools.decode(token)
    if payload is None:
        raise AuthException('Invalid token')
    if datetime.datetime.fromtimestamp(payload['exp']) < datetime.datetime.now():
        raise AuthException('Token expired')

    return UserToken.get_user(token)


def get_current_user_or_none(token: Annotated[str | None, Header()] = None) -> User | None:
    return None if token is None else get_current_user(token)
