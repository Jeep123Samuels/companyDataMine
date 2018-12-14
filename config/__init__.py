"""Config settings for app."""

import os

from dotenv import load_dotenv

dotenv_path: str = '.env'
load_dotenv(dotenv_path)

ACCESS_LOG: bool = os.getenv('ACCESS_LOG', False)
APP_NAME: str = os.getenv('APP_NAME', 'Default App')
APP_PORT: int = os.getenv('APP_PORT', 8000)
API_CONTACT_EMAIL: str = os.getenv('API_CONTACT_EMAIL')
API_VERSION: str = os.getenv('API_VERSION', '/api/v1')

DEBUG: bool = os.getenv('DEBUG', False)
LOGGING_LEVEL: str = os.getenv('LOGGING_LEVEL', 'DEBUG')
APP_ENVIRONMENT: str = os.getenv('APP_ENVIRONMENT', 'DEV')

# Services keys from env.
FULL_CONTACT_API_KEY: str = os.getenv('FULL_CONTACT_API_KEY')
MASHAPE_API_KEY: str = os.getenv('MASHAPE_API_KEY')
WHOIS_API_KEY: str = os.getenv('WHOIS_API_KEY')

FIREBASE_URL: str = os.getenv('FIREBASE_URL')
FIRE_BASE_JSON: str = os.getenv('FIRE_BASE_JSON')

# Postgres settings
database_mapping: dict = dict(
    DEV=os.getenv('DATABASE_NAME', 'default'),
    TEST=os.getenv('TEST_DATABASE_NAME', 'test_default'),
)
DATABASE_NAME: str = database_mapping[APP_ENVIRONMENT]
DB_USER: str = os.getenv('DB_USER')
DB_HOST: str = os.getenv('DB_HOST')
DB_PWD: str = os.getenv('DB_PWD')
DB_PORT: str = os.getenv('DB_PORT')
