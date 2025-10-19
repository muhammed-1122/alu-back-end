#!/usr/bin/python3
"""
Fetches all tasks from all employees and exports to a JSON file.
"""

import json
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"

    # Get all users
    users_res = requests.get(base_url + "users")
    if users_res.status_code != 200:
        print("Could not retrieve users.")
        sys.exit(1)

    users_data = users_res.json()

    # Get all TODOs
    todos_res = requests.get(base_url + "todos")
    if todos_res.status_code != 200:
        print("Could not retrieve TODO list.")
        sys.exit(1)

    todos_data = todos_res.json()

    # Create a dictionary to map user ID to username
    users_dict = {}
    for user in users_data:
        users_dict[user.get('id')] = user.get('username')

    # Prepare the final data structure
    all_employees_tasks = {}

    for task in todos_data:
        user_id = task.get('userId')
        username = users_dict.get(user_id)

        if not username:
            continue  # Skip if task has no matching user

        # Format the task dictionary
        task_dict = {
            "username": username,
            "task": task.get('title'),
            "completed": task.get('completed')
        }

        # Convert user_id to string for the JSON key
        user_id_str = str(user_id)

        # Append the task to the correct user's list
        if all_employees_tasks.get(user_id_str):
            all_employees_tasks[user_id_str].append(task_dict)
        else:
            all_employees_tasks[user_id_str] = [task_dict]

    # Define filename
    filename = "todo_all_employees.json"

    # Write data to JSON
    with open(filename, mode='w') as file:
        json.dump(all_employees_tasks, file)
