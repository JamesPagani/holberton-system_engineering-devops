#!/usr/bin/python3
"""How many subs?
Make a request to Reddit and find how many subscribers a subreddit has.
DOES NOT DISPLAY HOW MANY ACTIVE USERS A SUBREDDIT HAS.
"""


import requests


def number_of_subscribers(subreddit):
    """Return the amount of subscribers of a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'windows:subs:v1.1.0'}

    subreddit = requests.get(url, allow_redirects=False,
                             headers=headers)

    if subreddit.status_code >= 300:
        return 0

    sub_r_data = subreddit.json()
    subs = sub_r_data.get("data", 0).get("subscribers", 0)

    return subs
