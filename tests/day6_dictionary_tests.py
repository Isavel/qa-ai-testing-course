print("Running Day 6 tests")

test_cases = [
    {
        "response" : "Software testing ensures quality and reliability",
        "expected_word" : "quality"
    },
    {
        "response" : "Testing finds bugs",
        "expected_word" : "quality"
    },
    {
        "response": "Quality assurance improves software",
        "expected_word": "quality"
    }
]

def validate_response(test):
    
    response = test["response"]

    expected = test["expected_word"]

    if expected in response.lower():

        print("PASS: ", response)

    else:

        print("FAIL: ", response)

for test in test_cases:

    validate_response(test)