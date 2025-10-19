#!/usr/bin/python3
"""Exports data in JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)

    user = requests.get(url_user).json()
    todos = requests.get(url_todos).json()

    username = user.get("username")

    data = {
        str(emp_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            } for task in todos
        ]
    }

    filename = "{}.json".format(emp_id)
    with open(filename, "w") as f:
        json.dump(data, f)

