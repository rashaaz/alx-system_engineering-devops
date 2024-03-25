#!/usr/bin/python3
"""export data from a REST API for a given employee"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    us = requests.get(url + "users/{}".format(user_id)).json()
    username = us.get("username")
    to = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, tt.get("completed"), tt.get("title")]
            ) for tt in to]
