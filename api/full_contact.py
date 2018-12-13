"""Full Contact Search endpoints."""
from sanic import Blueprint, response

from config import API_VERSION
from services import firebase_custom, full_contact

blueprint_: object = Blueprint('search_full_contact', url_prefix=API_VERSION, strict_slashes=False)


@blueprint_.route('/search/full_contact/', methods=['GET'])
async def search_full_contact(request) -> dict:  # noqa: D103
    search_services: object = full_contact.FullContact()
    search_type: str = ''
    f_base: object = firebase_custom.f_base

    if 'email' in request.raw_args or 'twitter' in request.raw_args:
        search_type = 'search_person'
    elif 'domain' in request.raw_args:
        search_type = 'search_domain'

    if not search_type:
        return response.json({'message': 'Missing search query parameters.'}, status=400)

    key_ = list(request.raw_args.values())[0]
    firebase_data: dict = f_base.get_data(
        path=f'full_contact_{search_type}',
        key=key_,
    )
    if firebase_data:
        return response.json(firebase_data)

    fc_res: object = await getattr(search_services, search_type)(request.raw_args)

    f_base.post_data(path=f'full_contact_{search_type}', key=key_,  data=fc_res.json())

    return response.json(fc_res.json())
