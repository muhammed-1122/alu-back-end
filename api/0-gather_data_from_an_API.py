#!/usr/bin/python3
"""Returns information about an employee's TODO list progress"""
import requests
import sys


if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)

    user = requests.get(url_user).json()
    todos = requests.get(url_todos).json()

    name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task.get("title") for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(done_tasks), total_tasks))
    for title in done_tasks:
        print("\t {}".format(title))
