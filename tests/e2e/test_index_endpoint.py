"""Tests for search endpoint."""

from config import API_VERSION


async def test_return_expected_response_from_index_endpoint(test_client):
    """Should return expected response from index endpoint."""
    response = await test_client.get('{}/'.format(API_VERSION))
    json_resp = await response.json()
    assert response.status == 200
    assert json_resp['Hello'] == 'Something'
