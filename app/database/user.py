from __future__ import annotations

import datetime

from peewee import CharField, ForeignKeyField

from app.constant.user_token import UserTokenType
from app.database.base import BaseDatabaseModel
from app.tool import jwt_tools


class User(BaseDatabaseModel):
    class Meta:
        table_name = 'user_user'

    email = CharField(max_length=128, null=True)
    username = CharField(max_length=128, null=True)
    password = CharField(max_length=128, null=True)

    @classmethod
    def get_by_email(cls, email: str) -> User:
        return cls.select().where(cls.email == email).first()

    @classmethod
    def get_by_username(cls, username: str) -> User:
        return cls.select().where(cls.username == username).first()

    def check_password(self, password: str) -> bool:
        return self.password == password


class UserToken(BaseDatabaseModel):
    class Meta:
        table_name = 'user_user_token'

    user = ForeignKeyField(User, db_column='user_id', backref='token_list', null=True)
    token = CharField(max_length=1024, null=True)
    type = CharField(max_length=32, null=True)

    @classmethod
    def new_token(cls, user: User, token_type: UserTokenType) -> UserToken:
        payload = {
            'user_id': user.id,
            'name': user.username,
            'iat': datetime.datetime.utcnow().timestamp(),
            'exp': (datetime.datetime.utcnow() + datetime.timedelta(days=30)).timestamp(),
            'type': token_type.value
        }
        token = jwt_tools.encode(payload)
        user_token = cls(user=user, token=token, type=token_type.value)
        user_token.save()
        return user_token

    @classmethod
    def get_user(cls, token: str) -> User:
        item = cls.select().where(cls.token == token).first()
        return item.user if item else None
