"""Utils for sanic sandbox app."""

from functools import wraps


def format_to_firebase_key(input) -> str:
    """Formats a key into the correct format to be used in Firebase."""
    return input.replace('.', '_dot_').replace('@', '_at_')


async def auth_token_check(func):  # noqa: D103
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
