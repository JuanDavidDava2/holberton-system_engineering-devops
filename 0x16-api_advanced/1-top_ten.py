#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers.
"""
import requests


def top_ten(subreddit):
    data = ""
    if type(subreddit) is not str:
        data = "None\n"
    else:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {'user-agent': 'agent'}
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            data = "None\n"
        else:
            data_json = res.json().get("data").get("children")
            for i in range(10):
                data_title = data_json[i].get("data").get("title")
                data += "{}\n".format(data_title)
    print(data, end="")
