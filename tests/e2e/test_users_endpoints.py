"""Tests for Users endpoints."""

from config import API_VERSION


async def test_return_expected_response_from_users_get_endpoint(test_client):
    """Should return expected response from users GET endpoint."""
    response = await test_client.get('{}/users/'.format(API_VERSION))
    json_resp = await response.json()

    # email='',
    # username='',
    # password='',
    # is_active=True,
    # created_on='',
    # modified_on='',
    assert response.status == 200
    assert json_resp['message'] == 'Getting Users'
