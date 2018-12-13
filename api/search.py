"""Search endpoints."""

from sanic import Blueprint, response

from config import API_VERSION

blueprint_: object = Blueprint('search', url_prefix=API_VERSION, strict_slashes=False)


@blueprint_.route('/search/', methods=['GET'])
async def search(request) -> dict:
    """Search endpoint will combine all services and return a collective response for queries."""
    complete_response: dict = {}

    return response.json({'NOT_READY': 'Endpoint under construction. Check back later.'})
