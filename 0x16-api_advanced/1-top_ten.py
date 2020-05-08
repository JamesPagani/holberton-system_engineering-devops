#!/usr/bin/python3
"""Top ten
Make a request to Reddit and find the top 10 hot posts in a subreddit.
"""


import requests


def top_ten(subreddit):
    """Return the amount of subscribers of a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'user-agent': 'windows:subs:v1.1.0'}

    subreddit = requests.get(url, allow_redirects=False,
                             headers=headers)

    if subreddit.status_code != 200:
        print(None)
        return

    sub_json = subreddit.json()
    hot_posts = sub_json.get("data", None).get("children", None)

    for post in hot_posts:
        post_title = post.get("data", None).get("title", None)
        print(post_title)
