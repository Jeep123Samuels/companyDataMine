"""Users Model."""

from datetime import datetime

from peewee import (
    BooleanField,
    CharField,
    DateTimeField,
)

from database_psql.db_instance import BaseModel


class Users(BaseModel):  # noqa: D103
    email = CharField(unique=True)
    username = CharField(unique=True)
    password = CharField()
    is_active = BooleanField(default=True)
    created_on = DateTimeField(default=datetime.now())
    modified_on = DateTimeField(default=datetime.now())
