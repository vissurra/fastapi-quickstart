from pydantic import BaseModel, Field


class UserSignUpReq(BaseModel):
    email: str = Field(min_length=1, max_length=64)
    username: str = Field(min_length=1, max_length=64)
    password: str = Field(min_length=12, max_length=16)


class UserSignUpRes(BaseModel):
    user_id: int
    email: str
    username: str
    token: str


class UserSignInReq(BaseModel):
    email: str | None = Field(min_length=1, max_length=64)
    username: str | None = Field(min_length=1, max_length=64)
    password: str = Field(min_length=12, max_length=16)


class UserSignInRes(BaseModel):
    user_id: int
    email: str
    username: str
    token: str


class UserProfileRes(BaseModel):
    email: str
    username: str
