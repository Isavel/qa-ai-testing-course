print("Running Day 3 Tests")

test_cases = [
    "Software testing ensures quality",
    "Testing",
    "Quality assurance helps detect bugs",
    "QA improves software reliability",
    "Bugs"
]

for response in test_cases:

    if len(response) > 25:
        print("PASS: ", response)
    else:
        print("FAIL: ", response)