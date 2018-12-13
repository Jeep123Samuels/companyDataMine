"""Tests for WhoIs search endpoint."""

from config import API_VERSION


async def test_return_expected_response_from_whois_search_endpoint(test_client):
    """Should return expected response from company whois search endpoint."""
    # when ... a request is made to whois with valid search parameters
    response = await test_client.get(
        '{}/search/whois/?domain=fullcontact.com'.format(API_VERSION),
    )

    # then
    # ... return the response 200
    # ... and contains admin_contacts with FullContact Inc.
    json_resp = await response.json()
    assert response.status == 200
    assert json_resp['admin_contacts'][0]['organization'] == 'FullContact Inc.'
