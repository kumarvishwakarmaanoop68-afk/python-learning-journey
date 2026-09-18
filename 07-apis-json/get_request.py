# GET request example
# Install requests first with: pip install requests

import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    print("Title:", data["title"])
    print("Completed:", data["completed"])
except requests.RequestException as error:
    print("Request failed:", error)
