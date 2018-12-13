"""Mashape Api routing"""

from sanic import Blueprint, response

from config import API_VERSION
from services import firebase_custom, mashape_domain

blueprint_: object = Blueprint('search_mashape_domain', url_prefix=API_VERSION, strict_slashes=False)


@blueprint_.route('/search/mashape_domain/', methods=['GET'])
async def search_mashape_domain(request) -> dict:  # noqa: D103
    search_services: object = mashape_domain.MashapeDomain()
    f_base: object = firebase_custom.f_base

    firebase_data: dict = f_base.get_data(
        path='mashape_domain',
        key=request.raw_args['email'],
    )
    if firebase_data:
        return response.json(firebase_data)

    res: object = await search_services.get_domain_from_email(data=request.query_string)

    f_base.post_data(path='mashape_domain', key=request.raw_args['email'], data=res.json())

    return response.json(res.json())
