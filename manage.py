"""Manage commands for database."""
import sys
from peewee_async import Manager

from app_logger import logger
from database_psql.db_instance import app_database
from models import AuthTokens, Users

objects: object = Manager(app_database)
DB_TABLES: list = [AuthTokens, Users, ]


async def create_auth_user():
    try:
        await objects.create(Users, email='jeep123@gmail.com', username='jeep', password='password')
        await objects.create(AuthTokens, user=Users.select().where(username='jeep'), value='secret34876537285')
    except Exception as e:
        print(e.args)
        AuthTokens.drop_table(True)
        Users.drop_table(True)
        app_database.create_tables([AuthTokens, Users, ])
        user = await objects.create(Users, email='jeep123@gmail.com', username='jeep', password='password')
        await objects.create(AuthTokens, user=user, value='secret34876537285')

    finally:
        all_objects: object = await objects.execute(Users.select())
        _objects = await objects.execute(AuthTokens.select())

    for auth in _objects:
        print(auth.user)
        print(auth.value)
        print(auth.created_on)
    for obj in all_objects:
        print(obj.email)
        print(obj.username)
        print(obj.password)
        print(obj.id)
        print(dir(obj))


def create_tables() -> None:  # noqa: D103
    logger.info('Creating database tables...\n%s' % DB_TABLES)
    with objects.allow_sync():
        app_database.create_tables(DB_TABLES)
    logger.info('Completed creating database tables...')


def drop_tables() -> None:  # noqa: D103
    logger.info('Dropping database tables...')
    with objects.allow_sync():
        for table in DB_TABLES:
            table.drop_table(True)
            logger.info('Dropped table %s' % table.__name__)
    logger.info('Completed dropping database tables...')


options_dict = {
    'create_auth_user': create_auth_user,
    'create_tables': create_tables,
    'drop_tables': drop_tables,
}

if __name__ == '__main__':
    assert len(sys.argv) > 1, 'Missing command args:\nOPTIONS:\n"create_tables"\n"drop_tables"'
    assert len(sys.argv) < 3, 'Too many command args:\nOPTIONS:\n"create_tables"\n"drop_tables"'

    options_dict[sys.argv[-1]]()
