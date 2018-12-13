"""Unit tests for utils"""

import pytest

from utils import format_to_firebase_key


@pytest.mark.parametrize('input, expected', (
    ('@', '_at_'),
    ('.', '_dot_'),
    ('.@...', '_dot__at__dot__dot__dot_'),
    ('test.me@some.email.co.za', 'test_dot_me_at_some_dot_email_dot_co_dot_za'),

))
def test_format_input_correctly_for_firebase(input, expected):
    """Should format input correctly for firebase."""
    # when format_to_firebase_key is called for an input
    response = format_to_firebase_key(input)

    # then expect the results to be accepted by firebase
    assert response == expected
