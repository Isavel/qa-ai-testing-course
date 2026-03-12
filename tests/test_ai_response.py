print("Running AI Tests ")

responses = ["Software testing ensures product quality",
            "Testing",
            "Quality assurance improves software reliability" 
]

for response in responses:
    if len(response) > 20:
        print("Test PASS: ", response)
    else:
        print("Test FAIL: ", response)

print("Running AI Test 2 ")
response = "Testing"

if len(response) > 20:
    print("Test PASS...")
else:
    print("Test FAIL...")

print("Running test: in")
course = 'Python for beginners'

print('Python' in course)