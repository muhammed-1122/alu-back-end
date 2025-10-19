#!/usr/bin/env python3
import sys
import csv
import requests

if len(sys.argv) < 2:
    print("Usage: python 1-export_to_CSV.py <employee_id>")
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

# Export to CSV
output_file = f"{emp_id}.csv"
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for todo in todos:
        writer.writerow([
            emp_id,
            user["username"],
            todo["completed"],
            todo["title"]
        ])
