#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "My Reddit API Client (by /u/your_username)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        elif response.status_code == 404:
            print("Subreddit '{}' not found.".format(subreddit))
            return 0
        else:
            print("Error: {}".format(response.status_code))
            return 0
    except Exception as e:
        print("An error occurred: {}".format(e))
        return 0
