#!/usr/bin/python3
"""gather data from a REST API for a given employee ID and display"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    us = requests.get(url + "users/{}".format(sys.argv[1])).json()
    to = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    co = [tt.get("title") for tt in to if tt.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        us.get("name"), len(co), len(to)))
    [print("\t {}".format(cc)) for cc in co]
