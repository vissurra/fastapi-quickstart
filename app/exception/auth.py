from fastapi import HTTPException
from starlette import status


class AuthException(HTTPException):
    def __init__(self, message='Auth error'):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=message)
