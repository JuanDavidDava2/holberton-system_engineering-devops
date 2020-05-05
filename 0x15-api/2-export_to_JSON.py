#!/usr/bin/python3
"""
Using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys
import csv
import json

if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com'
    user_id = sys.argv[1]
    employee = requests.get('{}/users/{}'.format(url, user_id))
    username = employee.json().get('username')

    tasks = requests.get('{}/todos?userId={}'.format(url, user_id))
    task_list = tasks.json()
    json_dic = {user_id: [{"task": task.get('title'),
                           "completed": task.get('completed'),
                           "username": username}
                          for task in task_list]}

    with open('{}.json'.format(user_id), 'w') as a:
        json.dump(json_dic, a)
