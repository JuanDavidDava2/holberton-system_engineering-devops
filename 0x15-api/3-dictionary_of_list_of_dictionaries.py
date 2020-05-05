#!/usr/bin/python3
"""
Using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests

if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
             } for t in requests.get(url + "todos",
                                     params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
