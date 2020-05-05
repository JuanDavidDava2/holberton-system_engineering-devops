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
    employee = requests.get('{}/users/{}'.format(url, sys.argv[1]))
    employee_name = employee.json().get('name')

    tasks = requests.get('{}/todos?userId={}'.format(url, sys.argv[1]))
    task_list = tasks.json()
    row_list = [[sys.argv[1],
                employee_name,
                task.get('completed'),
                task.get('title')]
                for task in task_list]

    with open('{}.csv'.format(sys.argv[1]), 'w') as a:
        writer = csv.writer(a, quoting=csv.QUOTE_ALL)
        writer.writerows(row_list)
