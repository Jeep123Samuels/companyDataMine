"""E2e Tests for Mashape."""

from config import API_VERSION


async def test_return_success_response_for_mashape_endpoint(test_client):
    """Should return success response for mashape endpoint."""
    # when ... a request is made to mashape with valid search parameters
    response: object = await test_client.get(
        '{}/search/mashape_domain/?email=bart@fullcontact.com'.format(API_VERSION),
    )

    # then
    # ... return the response 200
    # ... and contains domain with fullcontact.com.
    json_resp: dict = await response.json()
    assert response.status == 200
    assert json_resp['valid']
    assert json_resp['domain'] == 'fullcontact.com'
