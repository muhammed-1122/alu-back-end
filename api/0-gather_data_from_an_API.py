#!/usr/bin/python3
"""
Fetches and displays TODO list progress for a given employee ID.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com/"

    # Get user information
    user_res = requests.get(base_url + "users/{}".format(emp_id))
    if user_res.status_code != 200:
        print("User not found.")
        sys.exit(1)

    user_data = user_res.json()
    emp_name = user_data.get('name')

    # Get user's TODO list
    todos_res = requests.get(base_url + "todos", params={'userId': emp_id})
    if todos_res.status_code != 200:
        print("Could not retrieve TODO list.")
        sys.exit(1)

    todos_data = todos_res.json()

    # Process tasks
    total_tasks = len(todos_data)
    done_tasks = []
    for task in todos_data:
        if task.get('completed') is True:
            done_tasks.append(task.get('title'))

    num_done_tasks = len(done_tasks)

    # Print the formatted output
    # Broke this print statement into variables to ensure PEP 8 compliance
    print_str = "Employee {} is done with tasks({}/{}):"
    print(print_str.format(emp_name, num_done_tasks, total_tasks))

    for title in done_tasks:
        print("\t {}".format(title))
