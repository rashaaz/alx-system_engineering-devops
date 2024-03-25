#!/usr/bin/python3
"""export data from a REST API for a given employee ID in JSON"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    us = requests.get(url + "users/{}".format(user_id)).json()
    username = us.get("username")
    to = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": tt.get("title"),
                "completed": tt.get("completed"),
                "username": username
                } for tt in to]}, jsonfile)
