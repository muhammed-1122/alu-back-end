#!/usr/bin/env python3
import json
import requests

# Fetch all users
users_url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(users_url)
response.raise_for_status()
users = response.json()

# Prepare dictionary for all employees
all_tasks = {}

for user in users:
    user_id = str(user["id"])
    username = user["username"]

    # Fetch this user's todos
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    response = requests.get(todos_url)
    response.raise_for_status()
    todos = response.json()

    # Format tasks as list of dictionaries
    all_tasks[user_id] = [
        {"username": username, "task": todo["title"], "completed": todo["completed"]}
        for todo in todos
    ]

# Export to JSON
with open("todo_all_employees.json", "w") as json_file:
    json.dump(all_tasks, json_file)
