#!/usr/bin/python3
"""Gather data from an API.
Given the ID of an employee, return its progress in his/her TODO list.
"""


import json
import requests
from sys import argv

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users/{}".format(api_url, argv[1])).json()
    todos = requests.get("{}users/{}/todos".format(api_url, argv[1])).json()

    user_id = user.get("id")
    username = user.get("username")

    user_tasks = []
    for task in todos:
        task_status = task.get("completed")
        task_title = task.get("title")
        user_tasks.append({"task": task_title, "completed": task_status,
                           "username": username})

    user_info = {user_id: user_tasks}

    with open("{}.json".format(user_id), mode="w") as json_file:
        json_file.write(json.dumps(user_info))
