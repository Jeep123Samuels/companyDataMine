"""Global fixtures for app."""

import pytest


@pytest.yield_fixture
def app() -> object:  # noqa: D103
    from sanic import Sanic

    from api import full_contact, index, mashape_domain, search, whois
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

    yield app


@pytest.fixture
def test_client(loop, app, test_client) -> object:
    return loop.run_until_complete(test_client(app))
