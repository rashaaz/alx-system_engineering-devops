#!/usr/bin/python3
"""Export data in the JSON format"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    us = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            uu.get("id"): [{
                "task": b.get("title"),
                "completed": b.get("completed"),
                "username": uu.get("username")
            } for b in requests.get(url + "todos",
                                    params={"userId": uu.get("id")}).json()]
            for uu in us}, jsonfile)
