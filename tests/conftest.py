"""Global fixtures for app."""

import os

from peewee_async import Manager, PostgresqlDatabase
import pytest

from manage import create_tables

from config import (
    DB_HOST,
    DB_PORT,
    DB_PWD,
    DB_USER,
    database_mapping,
)


@pytest.yield_fixture
def app() -> object:  # noqa: D103
    from sanic import Sanic

    from api import (
        full_contact,
        index,
        mashape_domain,
        search,
        users,
        whois,
    )
    from config import API_VERSION

    app: object = Sanic('Full Contact Sandbox')
    app.config.API_VERSION: str = API_VERSION
    app.config.API_TITLE: str = 'Sanic Sandbox Test'
    app.config.API_DESCRIPTION: str = 'Sanic Sandbox Test'
    app.config.API_PRODUCES_CONTENT_TYPES: list = ['application/json']
    app.config.API_CONTACT_EMAIL: str = 'jp.samuels@takectrl.co.za'

    app.blueprint(full_contact.blueprint_)
    app.blueprint(index.blueprint_)
    app.blueprint(mashape_domain.blueprint_)
    app.blueprint(search.blueprint_)
    app.blueprint(whois.blueprint_)

    app.add_route(users.UsersEndpoint.as_view(), f'{API_VERSION}/users/')

    yield app


@pytest.fixture
def db():
    db: object = PostgresqlDatabase(
        database_mapping['TEST'],
        user=DB_USER,
        password=DB_PWD,
        host=DB_HOST,
        port=DB_PORT,
    )
    print(database_mapping['TEST'])
    create_tables()

    yield Manager(db)


@pytest.fixture
def test_client(request, loop, app, db, test_client) -> object:

    def teardown():
        print(dir(db))
    request.addfinalizer(teardown)
    return loop.run_until_complete(test_client(app))
