from utils.validators import validate_length, validate_keyword

print("Running Day 7 Tests")

response = " Software testing ensures quality and reliability"

if validate_length(response,30):
    print("PASS Length ")
else:
    print("FAIL Length ")

if validate_keyword(response, "quality"):
    print("PASS keyword")
else:
    print("FAIL keyword")