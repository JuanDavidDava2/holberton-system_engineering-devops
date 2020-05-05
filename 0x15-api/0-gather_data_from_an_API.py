#!/usr/bin/python3
"""
Using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com'

    employee = requests.get('{}/users/{}'.format(url, sys.argv[1]))
    employee_name = employee.json().get('name')

    tasks = requests.get('{}/todos?userId={}'.format(url, sys.argv[1]))
    task_list = tasks.json()
    total_tasks = len(task_list)
    completed_tasks = sum(1 for task in task_list if task.get('completed'))

    print('Employee {} is done with tasks({}/{}):\
                        '.format(employee_name, completed_tasks, total_tasks))
    for task in task_list:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))
