# Day 7 API and JSON practice

import json

# 1. Convert a Python dictionary to JSON.
student = {"name": "Student", "course": "Python"}
json_text = json.dumps(student)
print("JSON:", json_text)

# 2. Convert JSON back to a Python dictionary.
data = json.loads(json_text)
print("Course:", data["course"])

# 3. Display common HTTP methods.
for method in ["GET", "POST", "PUT", "DELETE"]:
    print(method)
