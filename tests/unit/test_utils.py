"""Unit tests for utils"""

import pytest

from utils import check_valid_secure_str, encrypt_input_str, format_to_firebase_key


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


def test_return_correct_encrypted_string():
    """Should return correct encrypted string."""
    # when ... encrypted function is called with 'password' args
    encrypted_str = encrypt_input_str('password')

    # then ... expect following encrypted string to be returned.
    expected_encrypted = '5f4dcc3b5aa765d61d8327deb882cf99'
    assert encrypted_str == expected_encrypted


def test_return_valid_encrypted_string():
    """Should return valid encrypted string."""
    # when ... check encrypted function is called with 'password' args
    check_response = check_valid_secure_str(
        input_str='password',
        encrypted_str='5f4dcc3b5aa765d61d8327deb882cf99',
    )

    # then ... expect call to return True.
    assert check_response
