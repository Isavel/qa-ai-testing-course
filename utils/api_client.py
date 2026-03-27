import requests

def get_requests(url):
    """
    Send a GET request to the given URL

    Args:
    url (str): API endpoint

    Returns:
    Response OBJECT

    """
    return requests.get(url)

def get_json(url):
    """
    Send GET request and return JSON data
    """

    response = requests.get(url)

    return response.json()
