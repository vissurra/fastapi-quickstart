from typing import Annotated

from fastapi import APIRouter, Body, Depends

from app.constant.user_token import UserTokenType
from app.database.base import db
from app.database.user import User, UserToken
from app.dependency.user import get_current_user
from app.exception.auth import AuthException
from app.exception.biz import BizException
from app.model.user import UserSignUpRes, UserSignUpReq, UserSignInRes, UserSignInReq, UserProfileRes

router = APIRouter(
    prefix="/fastapi/user",
    tags=["user"]
)


@router.post('/sign_up', response_model=UserSignUpRes)
def sign_up(item: Annotated[UserSignUpReq, Body()]):
    if User.get_by_email(item.email) is not None:
        raise BizException('Email already exists')
    if User.get_by_username(item.username) is not None:
        raise BizException('Username already exists')

    with db.atomic():
        user = User(email=item.email, username=item.username, password=item.password)
        user.save()

        token_type = UserTokenType.NORMAL
        user_token = UserToken.new_token(user, token_type)

    res = UserSignUpRes(user_id=user.id, username=user.username, email=user.email, token=user_token.token)
    return res


@router.post('/sign_in', response_model=UserSignInRes)
def sign_in(item: Annotated[UserSignInReq, Body()]):
    if item.email is not None:
        user = User.get_by_email(item.email)
    elif item.username is not None:
        user = User.get_by_username(item.username)
    else:
        raise AuthException('Email or username is required')

    if user is None:
        raise AuthException('User not found')
    if not user.check_password(item.password):
        raise AuthException('Password is incorrect')

    token_type = UserTokenType.NORMAL
    user_token = UserToken.new_token(user, token_type)

    res = UserSignUpRes(user_id=user.id, username=user.username, email=user.email, token=user_token.token)
    return res


@router.get('/profile')
def get_profile(user: Annotated[User, Depends(get_current_user)]):
    res = UserProfileRes(username=user.username, email=user.email)
    return res
