#!/usr/bin/python3
"""Gather data from an API.
Given the ID of an employee, return its progress in his/her TODO list.
"""



import requests
from sys import argv


def completed_tasks(user_tasks):
    """Count the amount of completed tasks in the user's TODO list."""
    completed = 0

    for task in user_tasks:
        if task.get("completed") is True:
            completed += 1

    return completed

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users/{}".format(api_url, argv[1])).json()
    todos = requests.get("{}users/{}/todos".format(api_url, argv[1])).json()

    name = user.get("name")
    tasks_done = completed_tasks(todos)
    tasks_total = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(name, tasks_done,
                                                          tasks_total))
    for task in todos:
        if task.get("completed") is True:
            print("\t {}".format(task.get("title")))
