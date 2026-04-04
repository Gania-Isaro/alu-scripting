#!/usr/bin/python3
"""
Fetch and print top 10 hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:api_advanced:v1.0.0 (by /u/antigravity)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            posts = response.json().get('data').get('children')
            for post in posts:
                print(post.get('data').get('title'))
        else:
            print(None)
    except Exception:
        print(None)
