#!/usr/bin/python3
"""Function that queries the Reddit API and returns
 the number of subscribers for a given subreddit."""
import requests

url = 'https://www.reddit.com/r/{}/about.json'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}


def number_of_subscribers(subreddit):
    """Returns number of subscribers"""
    req = requests.get(url.format(subreddit), headers=headers)
    if req.status_code == 200:
        return(req.json()['data']['subscribers'])
    return 0
