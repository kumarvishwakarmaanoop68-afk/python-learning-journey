# Common HTTP methods

methods = {
    "GET": "Read data",
    "POST": "Create data",
    "PUT": "Update existing data",
    "DELETE": "Delete data"
}

for method, purpose in methods.items():
    print(f"{method}: {purpose}")
