"""Config settings for app."""

import os

from dotenv import load_dotenv

dotenv_path: str = '.env'
load_dotenv(dotenv_path)

ACCESS_LOG: bool = os.getenv('ACCESS_LOG', False)
APP_PORT: int = os.getenv('APP_PORT', 8000)
API_CONTACT_EMAIL: str = os.getenv('API_CONTACT_EMAIL')
API_VERSION: str = os.getenv('API_VERSION', '/api/v1')

DEBUG: bool = os.getenv('DEBUG', False)

# Services keys from env.
FULL_CONTACT_API_KEY: str = os.getenv('FULL_CONTACT_API_KEY')
MASHAPE_API_KEY: str = os.getenv('MASHAPE_API_KEY')
WHOIS_API_KEY: str = os.getenv('WHOIS_API_KEY')

FIREBASE_URL: str = os.getenv('FIREBASE_URL')
FIRE_BASE_JSON: str = os.getenv('FIRE_BASE_JSON')
