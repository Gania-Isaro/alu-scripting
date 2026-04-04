#!/usr/bin/python3
"""
Fetch and print top 10 hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:topten:v1.0 (by /u/fakeuser123)"
    }
    params = {"limit": 10}

    try:
        res = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if res.status_code != 200:
            print(None)
            return

        posts = res.json().get("data", {}).get("children", [])
        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)