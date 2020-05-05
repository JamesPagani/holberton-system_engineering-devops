#!/usr/bin/python3
"""Gather data from an API.
Given the ID of an employee, return its progress in his/her TODO list.
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users/{}".format(api_url, argv[1])).json()
    todos = requests.get("{}users/{}/todos".format(api_url, argv[1])).json()

    user_id = argv[1]
    user_name = user.get("username")

    with open("{}.csv".format(user_id), mode='w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todos:
            task_status = task.get("completed")
            task_title = task.get("title")
            writer.writerow([user_id, user_name, task_status, task_title])
