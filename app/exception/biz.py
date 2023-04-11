from fastapi import HTTPException
from starlette import status


class BizException(HTTPException):
    def __init__(self, message):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=message)
