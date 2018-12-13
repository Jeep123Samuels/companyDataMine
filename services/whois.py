"""Full Contact Service"""

import json
import requests

from config import WHOIS_API_KEY


class WhoIs(object):
    """Factory class for Whois service."""
    base_url: str = 'https://jsonwhois.com/api/v1/whois'
    headers: dict = {
        'content-type': 'application/json',
        'Authorization': f'Token token={WHOIS_API_KEY}',
    }

    async def search_domain(self, data) -> object:
        return requests.get(
            url=self.base_url,
            data=json.dumps(data) or {},
            headers=self.headers,
        )
