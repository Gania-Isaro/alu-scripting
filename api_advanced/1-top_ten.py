#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries title of first 10 hot posts.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'linux:api_advanced:v1.0.0 (by /u/antigravity)'
    }
    params = {'limit': 10}

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
