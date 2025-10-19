#!/usr/bin/python3
"""Exports data in CSV format"""
import csv
import requests
import sys


if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)

    user = requests.get(url_user).json()
    todos = requests.get(url_todos).json()

    username = user.get("username")

    filename = "{}.csv".format(emp_id)
    with open(filename, mode="w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                emp_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
