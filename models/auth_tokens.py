"""AuthToken Model."""

from datetime import datetime

from peewee import (
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKeyField,
)

from database_psql.db_instance import BaseModel
from models.users import Users


class AuthTokens(BaseModel):  # noqa: D103
    user = ForeignKeyField(Users)
    value = CharField()
    is_active = BooleanField(default=True)
    created_on = DateTimeField(default=datetime.now())
    modified_on = DateTimeField(default=datetime.now())
