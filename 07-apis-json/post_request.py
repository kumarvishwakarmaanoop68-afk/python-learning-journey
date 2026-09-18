# POST request example
# Install requests first with: pip install requests

import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Python API Practice",
    "body": "Learning POST requests",
    "userId": 1
}

try:
    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()

    print("Status:", response.status_code)
    print("Response:", response.json())
except requests.RequestException as error:
    print("Request failed:", error)
