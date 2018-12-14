"""Utils for sanic sandbox app."""

from functools import wraps
from _md5 import md5


def format_to_firebase_key(input) -> str:
    """Formats a key into the correct format to be used in Firebase."""
    return input.replace('.', '_dot_').replace('@', '_at_')


def encrypt_input_str(input_str: str) -> str:
    """Encrypt any input string."""
    return md5(input_str.encode('utf-8')).hexdigest()


def check_valid_secure_str(input_str: str, encrypted_str: str) -> bool:
    """Check input str is equal to encrypted."""
    return encrypt_input_str(input_str) == encrypted_str


def check_valid_auth_token(token: str = '') -> bool:
    """Check input str is equal to user token."""
    return


async def auth_token_check(func) -> any:  # noqa: D103
    @wraps(func)
    def check_token(request, *args, **kwargs):
        if 'Authorization' not in request.headers:
            return (
                'Access denied\n', 403,
            )
        token = request.headers.get('Authorization')
        if not check_valid_auth_token(token):
            return (
                'AuthToken expired.\nPlease refresh.\n', 403,
            )
        # Otherwise just send them where they wanted to go
        return func(*args, **kwargs)
    return check_token
