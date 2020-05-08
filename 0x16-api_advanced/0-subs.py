#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    if type(subreddit) is not str:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'agent'}
    data = requests.get(url, headers=headers).json()
    try:
        return (data.get('data').get('subscribers'))
    except:
        return 0
