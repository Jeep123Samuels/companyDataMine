"""WhoIs Search endpoints."""
from sanic import Blueprint, response

from config import API_VERSION
from services import firebase_custom, whois

blueprint_: object = Blueprint('search_whois', url_prefix=API_VERSION, strict_slashes=False)


@blueprint_.route('/search/whois/', methods=['GET'])
async def search_whois(request) -> dict:  # noqa: D103
    search_services: object = whois.WhoIs()
    if 'domain' not in request.raw_args:
        return response.json({'message': 'Missing search query parameters.'}, status=400)
    f_base: object = firebase_custom.f_base

    firebase_data: dict = f_base.get_data(
        path='whois',
        key=request.raw_args['domain'],
    )
    if firebase_data:
        return response.json(firebase_data)

    whois_res: object = await search_services.search_domain(data=request.raw_args)

    f_base.post_data(path='whois', key=request.raw_args['domain'],  data=whois_res.json())

    return response.json(whois_res.json())
