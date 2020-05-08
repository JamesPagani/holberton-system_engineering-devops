#!/usr/bin/python3
"""How many subs?
Make a request to Reddit and find how many subscribers a subreddit has.
DOES NOT DISPLAY HOW MANY ACTIVE USERS A SUBREDDIT HAS.
"""


import requests


def number_of_subscribers(subreddit):
    """Return the amount of subscribers of a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'web:0x16-0.how_many_subs:v0.1.0'}

    subreddit = requests.get(url, allow_redirects=False, headers=headers).json()
    subs = subreddit.get("subscribers", 0)

    return subs
