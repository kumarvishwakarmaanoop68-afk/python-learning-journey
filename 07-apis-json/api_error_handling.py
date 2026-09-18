# Basic API error handling
# Install requests first with: pip install requests

import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    print("Success:", response.json())
except requests.Timeout:
    print("Request timed out.")
except requests.HTTPError as error:
    print("HTTP error:", error)
except requests.RequestException as error:
    print("Request error:", error)
