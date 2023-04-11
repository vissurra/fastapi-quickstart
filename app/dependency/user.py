import datetime
from typing import Annotated

from fastapi import Header

from app.database.user import User, UserToken
from app.exception.auth import AuthException
from app.tool import jwt_tools


def current_user(token: Annotated[str | None, Header()]) -> User:
    payload = jwt_tools.decode(token)
    if payload is None:
        raise AuthException('Invalid token')
    if datetime.datetime.fromtimestamp(payload['exp']) < datetime.datetime.now():
        raise AuthException('Token expired')

    return UserToken.get_user(token)
