#!/usr/bin/python3
"""
Fetches employee TODO list data and exports it to a CSV file.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com/"

    # Get user information
    user_res = requests.get(base_url + "users/{}".format(user_id))
    if user_res.status_code != 200:
        print("User not found.")
        sys.exit(1)

    user_data = user_res.json()
    username = user_data.get('username')

    # Get user's TODO list
    todos_res = requests.get(base_url + "todos", params={'userId': user_id})
    if todos_res.status_code != 200:
        print("Could not retrieve TODO list.")
        sys.exit(1)

    todos_data = todos_res.json()

    # Define filename
    filename = "{}.csv".format(user_id)

    # Write data to CSV
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            writer.writerow([
                user_id,
                username,
                task.get('completed'),
                task.get('title')
            ])
