#!/usr/bin/python3
"""
Using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys
import csv

if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com'
    user_id = sys.argv[1]
    employee = requests.get('{}/users/{}'.format(url, user_id ))
    employee_name = employee.json().get('name')

    tasks = requests.get('{}/todos?userId={}'.format(url, user_id))
    task_list = tasks.json()
    row_list = [[user_id,
                employee_name,
                task.get('completed'),
                task.get('title')]
                for task in task_list]

    with open('{}.csv'.format(user_id), 'w') as a:
        writer = csv.writer(a, quoting=csv.QUOTE_ALL)
        writer.writerows(row_list)
