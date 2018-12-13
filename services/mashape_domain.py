"""Mashape Api Service."""

import requests

from config import MASHAPE_API_KEY


class MashapeDomain(object):
    """Factory class for MashapeDomain service."""
    base_url: str = 'https://metropolis-api-email.p.mashape.com/analysis?{}'
    headers: dict = {
        'Accept': 'application/json',
        'X-Mashape-Key': MASHAPE_API_KEY,
    }

    async def get_domain_from_email(self, data) -> object:
        return requests.get(url=self.base_url.format(data), headers=self.headers)
