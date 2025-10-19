#!/usr/bin/env python3
import sys
import json
import requests

if len(sys.argv) < 2:
    print("Usage: python 2-another_script.py <employee_id>")
    sys.exit(1)

emp_id = int(sys.argv[1])

# Fetch user info
user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
response = requests.get(user_url)
response.raise_for_status()
user = response.json()

# Fetch user's TODO list
todos_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"
response = requests.get(todos_url)
response.raise_for_status()
todos = response.json()

# Structure the data
data = {
    str(emp_id): [
        {
            "username": user["username"],
            "task": todo["title"],
            "completed": todo["completed"]
        }
        for todo in todos
    ]
}

# Export to JSON
output_file = f"{emp_id}.json"
with open(output_file, "w") as jsonfile:
    json.dump(data, jsonfile)
