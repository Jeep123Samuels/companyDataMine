"""Database initial."""

from peewee import Model
from peewee_async import PostgresqlDatabase

from config import (
    DATABASE_NAME,
    DB_HOST,
    DB_PORT,
    DB_PWD,
    DB_USER,
)

app_database: object = PostgresqlDatabase(
    DATABASE_NAME,
    user=DB_USER,
    password=DB_PWD,
    host=DB_HOST,
    port=DB_PORT,
)


class BaseModel(Model):
    class Meta:
        database: object = app_database
