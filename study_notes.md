## Study Notes

### Day 1

* Installed Python
* Configured VS Code
* Ran first Python script
* Learned basic execution of Python files

### Day 2

* Created first Python test scripts
* Learned basic validation using `if` statements
* Initialized Git repository
* Created GitHub repository
* Pushed first code to GitHub

### Day 3

* Learned Python lists
* Used `for` loops to run multiple tests
* Executed automated test cases using loops

### Day 4

* Learned Python functions
* Created reusable validation functions
* Used functions to structure test logic
* Executed automated tests using functions

### Day 5

Project organization

Learned how to structure a QA automation project.

Created folders:

* tests
* data
* utils

Understood how professional repositories are organized.

Added:

* README.md
* requirements.txt

Moved test scripts into the `tests` folder.

Learned that Git does not track empty folders and used `.gitkeep`.

---

### Day 6

Python dictionaries and test datasets

Learned how to use dictionaries to structure test data.

Example:

test_case = {
"response": "Software testing ensures quality",
"expected_word": "quality"
}

Created datasets with multiple test cases.

Used dictionaries to simulate structured test inputs.

This structure is commonly used in:

* automated testing
* API testing
* AI / LLM evaluation datasets.

---

### Day 7

Python modules and reusable utilities

Learned how to separate reusable logic into modules.

Created:

utils/validators.py

Added reusable validation functions:

* validate_length()
* validate_keyword()

Imported functions into test scripts using:

from utils.validators import validate_length, validate_keyword

Executed tests using module execution:

python3 -m tests.day7_module_tests

Learned basic project architecture for automation testing.

Structure now includes:

tests → test scripts
utils → reusable validation logic
data → test datasets

### Day 8

API Testing and Code Documentation

Learned what an API is and how it is used for communication between systems.

Understood API testing concepts:

* Validating status codes (200, 404, etc.)
* Validating response content
* Validating response structure

Learned to use the `requests` library to send HTTP requests in Python.

Example:

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

Worked with JSON data using:

* response.json()

Created API test functions:

* test_api_status()
* test_response_length()

Validated:

* Status code is 200
* Response contains data

Added a new validation:

* Checked if response contains expected fields (e.g., userId)

---

Code Documentation

Learned to write professional docstrings in functions.

Example:

def test_api_status():
"""
Test that API returns status code 200.
"""

Understood importance of documenting:

* what the function does
* inputs
* expected behavior

---

Key Concepts

QA:

* API testing fundamentals
* validation of responses
* test coverage basics

Python:

* requests library
* JSON handling
* writing structured test functions

Best Practices:

* reusable functions
* readable code
* documentation with docstrings
---

### Day 9

Reusable API Client and Basic Framework Structure

Learned how to avoid code duplication by creating reusable functions.

Introduced the concept of abstraction in QA automation:

* Moving repeated logic into reusable modules

Created a new utility file:

* utils/api_client.py

Implemented a reusable function:

def get_request(url):
"""
Send a GET request to the given URL.
"""
return requests.get(url)

Updated test scripts to use the API client instead of calling requests directly.

Example:

from utils.api_client import get_request

response = get_request(url)

Improved test readability and maintainability.

---

Extended API client functionality

Created an additional helper function:

def get_json(url):
"""
Send GET request and return JSON data.
"""
response = get_request(url)
return response.json()

Used this function to simplify test logic.

---

Key Concepts

QA:

* abstraction in test automation
* reusable components
* maintainable test design

Python:

* modularization
* importing custom modules
* function reuse

Best Practices:

* avoid duplicated code
* separate test logic from request logic
* organize code into layers (tests vs utils)

---

Project Structure Update

tests → test cases
utils → API client + validators
data → test datasets

Project now follows a basic test automation architecture

---

### Day 10 

Advanced API Validations (QA Real Approach)

Learned how to perform deeper API validations beyond status codes.

Understood different validation levels in QA:

* Basic: status code validation
* Intermediate: response structure validation
* Advanced: data types and business logic validation

---

Implemented multiple validation types:

Validated response structure:

* Checked required fields exist (userId, id, title, body)

Validated data types:

* userId is integer
* title is string

Validated content:

* Ensured fields are not empty

Validated business rules:

* userId is greater than 0

---

Introduced reusable validation functions

Moved common validation logic to:

* utils/validators.py

Created reusable validators:

def validate_fields_exist(data, required_fields):
# returns missing fields

def validate_type(value, expected_type):
# checks data type

def validate_not_empty(value):
# checks if value is not empty

def validate_greater_than(value, threshold):
# checks business rule

---

Refactored test code

Separated:

* test logic (tests/)
* validation logic (utils/validators.py)

Improved:

* readability
* maintainability
* scalability

---

Key Concepts

QA:

* deep validation strategies
* structure vs content validation
* business logic validation

Python:

* reusable functions
* modular design
* cleaner imports

Best Practices:

* avoid duplicated validation logic
* use helper functions
* separate concerns (tests vs validations)

---

Project Evolution

Project now includes:

tests → test cases
utils → API client + validators
data → datasets

Project is evolving into a mini test automation framework


## Week 1 Key Concepts

### QA:
- test validation
- expected vs actual result
- test datasets

### Python:
- lists
- loops
- functions
- dictionaries
- modules

### Tools:
- Git
- GitHub
- VS Code


## Week 2 Key Concepts

### API

An **API** is a contract that enables communication between software components through well-defined request and response structures, typically over HTTP, allowing systems to exchange data in a standardized and decoupled way.

### Common HTTP Status Code Classes
- 1xx Informational: The request has been received and the process is continuing. These are temporary, non-final responses.
- 2xx Success: The request was successfully received, understood, and processed.
- 3xx Redirection: Further action needs to be taken by the client to complete the request, usually involving a change of URL or method.
- 4xx Client Error: The request contains bad syntax or cannot be fulfilled due to an issue on the client's end.
- 5xx Server Error: The server failed to fulfill a valid request due to an internal problem.
