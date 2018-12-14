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

    def __repr__(self):
        return f'<User:{self.username}, {self.email}, Active -> {self.is_active}>'

    def instance_to_dict(self) -> dict:
        return dict(
            email=self.email,
            username=self.username,
            is_active=self.is_active,
            created_on=self.created_on.isoformat(),
            modified_on=self.modified_on.isoformat(),
        )
