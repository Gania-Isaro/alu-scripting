#!/usr/bin/python3
"""
Fetch and print top 10 hot posts of a subreddit.
"""
import requests


def top_ten(subreddit):
    """Query Reddit and print the first 10 hot post titles."""
    url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])
        if not posts:
            print(None)
            return

        for post in posts[:10]:
            title = post.get("data", {}).get("title")
            if title:
                print(title)
    except Exception:
        print(None)
