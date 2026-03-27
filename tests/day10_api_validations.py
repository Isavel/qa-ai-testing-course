from utils.api_client import get_request
from utils.validators import (
    validate_fields_exist,
    validate_type,
    validate_not_empty,
    validate_greater_than
)

URL = "https://jsonplaceholder.typicode.com/posts"


def test_status_code():
    response = get_request(URL)

    assert response.status_code == 200, "Status code should be 200"


def test_response_structure():
    response = get_request(URL)
    data = response.json()
    first_item = data[0]

    required_fields = ["userId", "id", "title", "body"]

    missing = validate_fields_exist(first_item, required_fields)

    assert not missing, f"Missing fields: {missing}"


def test_data_types():
    response = get_request(URL)
    data = response.json()
    first_item = data[0]

    assert validate_type(first_item["userId"], int), "userId should be int"
    assert validate_type(first_item["title"], str), "title should be string"


def test_content_not_empty():
    response = get_request(URL)
    data = response.json()
    first_item = data[0]

    assert validate_not_empty(first_item["title"]), "title should not be empty"


def test_business_logic():
    response = get_request(URL)
    data = response.json()
    first_item = data[0]

    assert validate_greater_than(first_item["userId"], 0), "userId should be > 0"


test_status_code()
test_response_structure()
test_data_types()
test_content_not_empty()
test_business_logic()