# """Tests for search endpoint."""
#
# import pytest
#
# from config import API_VERSION
#
#
# @pytest.mark.parametrize('payload', (
#     'email=bart@fullcontact.com',
#     'twitter=@bartlorang',
# ))
# async def test_return_expected_response_from_person_full_contact_search_endpoint(
#     test_client,
#     payload: str,
# ):
#     """Should return expected response from person full_contact search endpoint."""
#     # when ... a request is made with valid search parameters
#     response = await test_client.get(
#         '{0}/search/full_contact/?{1}'.format(API_VERSION, payload),
#     )
#
#     # then
#     # ... return the response 200
#     # ... and contains fullName Bart Lorang
#     json_resp: dict = await response.json()
#     assert response.status == 200
#     assert json_resp['fullName'] == 'Bart Lorang'
#
#
# async def test_return_expected_response_from_company_full_contact_search_endpoint(test_client):
#     """Should return expected response from company full_contact search endpoint."""
#     # when ... a request is made with valid search parameters
#     response = await test_client.get(
#         '{}/search/full_contact/?domain=fullcontact.com'.format(API_VERSION),
#     )
#
#     # then
#     # ... return the response 200
#     # ... and contains name FullContact Inc.
#     json_resp: dict = await response.json()
#     assert response.status == 200
#     assert json_resp['name'] == 'FullContact Inc.'
#
#
# async def test_return_bad_request_response_person_full_contact_search_endpoint(test_client):
#     """Should return bad request response from person full_contact search endpoint."""
#     # when ... a request is made with no valid search parameters
#     response = await test_client.get(
#         '{}/search/full_contact/?something=fullcontact.com'.format(API_VERSION),
#     )
#
#     # then
#     # ... return the response 400
#     # ... and contains message 'Missing search query parameters'.
#     json_resp: dict = await response.json()
#     assert response.status == 400
#     assert json_resp['message'] == 'Missing search query parameters.'
