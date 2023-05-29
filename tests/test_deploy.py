import requests
import pytest

# This should match the api server name in the docker-compose file and the container port
base_url = "http://apiserver:80"

# Define a test function that takes a parameter
@pytest.mark.parametrize("id", [1, 2, 3])
def test_get_endpoint(id):
    # Make a GET request to the endpoint with the id
    response = requests.get(f"{base_url}/users/{id}")
    # Assert that the status code is 200
    assert response.status_code == 200
    # Assert that the response body is a JSON object
    assert response.headers["Content-Type"] == "application/json"
    # Assert that the response body has the expected fields
    data = response.json()
    assert "name" in data
    assert "id" in data