"""Index endpoint."""

from sanic import Blueprint, response

from config import API_VERSION


blueprint_: object = Blueprint('index', url_prefix=API_VERSION, strict_slashes=False)


@blueprint_.route('/', methods=['GET'])
async def index(request) -> dict:    # noqa: D103
    return response.json({'Hello': 'Something'})
