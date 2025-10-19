#!/usr/bin/env python3
import sys
import requests
import json

# Get employee ID from command line argument
if len(sys.argv) < 2:
    print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

emp_id = int(sys.argv[1])

# Fetch employee info
user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
response = requests.get(user_url)
response.raise_for_status()
user = response.json()

# Fetch user's TODO list
todos_url = (
    f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"
)
response = requests.get(todos_url)
response.raise_for_status()
todos = response.json()

# Prepare JSON output
tasks = [
    {
        "task": todo["title"],
        "completed": todo["completed"],
        "username": user["username"]
    }
    for todo in todos
]

output_file = f"{emp_id}.json"
with open(output_file, "w") as f:
    json.dump({str(emp_id): tasks}, f)
