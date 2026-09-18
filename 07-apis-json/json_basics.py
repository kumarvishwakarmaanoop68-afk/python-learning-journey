# JSON basics using Python's json module

import json

student = {
    "name": "Student",
    "course": "Diploma IT",
    "skills": ["Python", "C++"]
}

json_data = json.dumps(student, indent=4)
print("JSON data:")
print(json_data)

python_data = json.loads(json_data)
print("\nName:", python_data["name"])
print("Skills:", python_data["skills"])
