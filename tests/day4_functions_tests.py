print("Running Day 4 Tests")

def validate_response(response):

    if "quality" in response.lower():
        
        print("PASS: ", response)
    
    else:
        print("FAIL: ", response)

test_cases = [
    "Software testing ensures quality",
    "Testing",
    "Quality assurance helps detect bugs",
    "QA improves software reliability",
    "Bug"
]

for response in test_cases:

    validate_response(response)