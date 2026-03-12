print("# 2. Ejemplo práctico QA")

print("Running Day 2 Tests")

response = "software testing ensures product quality"

print("Response: ", response)

print("length: ", len(response))

print("# 3. Primera validación usando variables")

if len(response) > 30 :
    print("PASS: Response length valid")
else:
    print("FAIL: Response too short")

print("#4. Simular varios test cases")

response1 = "Software testing ensures product quality"
response2 = "Testing"
response3 = "Quality assurance helps detect bugs before release"

if len(response1) > 30:
    print("PASS")
else: 
    print("FAIL")

if len(response2) > 30:
    print("PASS")
else:
    print("FAIL")

if len(response3) > 30:
    print("PASS")
else:
    print("FAIL")