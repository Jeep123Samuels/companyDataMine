"""Users Endpoint."""

from sanic import response, views

from database_psql import db_instance
from models import Users


class UsersEndpoint(views.HTTPMethodView):
    """Users CRUD endpoints."""

    async def get(self, request):
        return response.json({'message': 'Getting Users'})

    async def post(self, request):
        return response.json({'message': 'User created'}, 201)

    async def put(self, request):
        pass

    async def patch(self, request):
        pass

    async def delete(self, request):
        pass


