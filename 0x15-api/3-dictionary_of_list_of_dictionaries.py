#!/usr/bin/python3
"""Dictionary of list of dictionaries.
Gathers the TODO list progress of ALL employes and saves it into a JSON file.
    JSON file: todo_all_employes.json
"""


import json
import requests

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get("{}users".format(api_url)).json()

    users_info = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        todo = requests.get("{}users/{}/todos".format(api_url, user_id)).json()

        user_tasks = []
        for task in todo:
            task_status = task.get("completed")
            task_title = task.get("title")
            user_tasks.append({"username": username, "task": task_title,
                               "completed": task_status})

        users_info[user_id] = user_tasks

    with open("todo_all_employees.json", mode="w") as json_file:
        json_file.write(json.dumps(users_info))
