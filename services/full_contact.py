"""Full Contact Service"""

import json
import requests

from config import FULL_CONTACT_API_KEY


class FullContact(object):
    """Factory class for FullContact service."""
    base_url: str = 'https://api.fullcontact.com/v3'
    headers: dict = {
        'content-type': 'application/json',
        'Authorization': f'Bearer {FULL_CONTACT_API_KEY}',
    }

    async def search_person(self, data=None) -> object:
        return requests.post(
            url=f'{self.base_url}/person.enrich',
            data=json.dumps(data) or {},
            headers=self.headers,
        )

    async def search_domain(self, data=None) -> object:
        return requests.post(
            url=f'{self.base_url}/company.enrich',
            data=json.dumps(data) or {},
            headers=self.headers,
        )
