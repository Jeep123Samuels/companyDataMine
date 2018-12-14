"""App script for Sandbox"""
from sanic import Sanic

from api import (
    full_contact,
    index,
    mashape_domain,
    search,
    users,
    whois,
)
from config import API_VERSION, API_CONTACT_EMAIL, APP_NAME


app: object = Sanic(APP_NAME)
app.config.API_VERSION: str = API_VERSION
app.config.API_TITLE: str = APP_NAME
app.config.API_DESCRIPTION: str = APP_NAME
app.config.API_PRODUCES_CONTENT_TYPES: list = ['application/json']
app.config.API_CONTACT_EMAIL: str = API_CONTACT_EMAIL


app.blueprint(full_contact.blueprint_)
app.blueprint(index.blueprint_)
app.blueprint(mashape_domain.blueprint_)
app.blueprint(search.blueprint_)
app.blueprint(whois.blueprint_)

app.add_route(users.UsersEndpoint.as_view(), f'{API_VERSION}/users/')
