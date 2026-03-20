import requests

print("Running Day 8 API tests")

def test_api_status():
    """
    Test that API returns status code 200.
    """

    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if(response.status_code == 200):
        print("PASS: Status code is 200")
    else:
        print("FAIL: Status code is not 200")

def test_response_length():

    """
    Test that API returns multiple records.
    """
    
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    data = response.json()

    if len(data) > 0:
        print("PASS: Response contains data")
    else:
        print("FAIL: Response is empty")

def test_first_post_structure():

    """
    Test the first post contains userId
    """

    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    data = response.json()

    if "userId" in data[0]:
        print("PASS: userId exists")
    else:
        print("FAIL: userId missing")





test_api_status()
test_response_length()
test_first_post_structure()
