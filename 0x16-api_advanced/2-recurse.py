#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit."""
import requests

url = 'https://www.reddit.com/r/{}/hot.json?after={}'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}


def recurse(subreddit, hot_list=[], next_page=""):
    """Returns all hot articles"""
    req = requests.get(url.format(subreddit, next_page), headers=headers)
    if req.status_code == 200:
        for item in req.json().get('data').get('children'):
            hot_list.append(item['data']['title'])
        next_page = req.json().get('data').get('after')
        if next_page:
            recurse(subreddit, hot_list, next_page)
        return hot_list
    else:
        return(None)
