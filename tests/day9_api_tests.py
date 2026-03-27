from utils.api_client import get_requests, get_json

print("Running Day 9 API Tests")

def test_api_status():
    """
    Validate API status code is 200
    """

    url = "https://jsonplaceholder.typicode.com/posts"

    response = get_requests(url)

    if response.status_code == 200:
        print("PASS : status code is 200")
    else:
        print("FAIL: status code is not 200")

def test_response_not_empty():
    """
    Validate API returns data
    """

    url = "https://jsonplaceholder.typicode.com/posts"

    data = get_json(url)

    if len(data) > 0:
        print("PASS: Response contains data")
    else:
        print("FAIL : Response is empty")

test_api_status()
test_response_not_empty()

