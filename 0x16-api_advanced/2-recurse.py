#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit."""
import requests

url = 'https://www.reddit.com/r/{}/hot.json'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}


def recurse(subreddit, hot_list=[], cont=0):
    """Returns all hot articles"""
    req = requests.get(url.format(subreddit), headers=headers)
    if req.status_code != 404:
        arts = req.json()['data']['children']
        if cont == len(arts) - 1:
            return hot_list
        hot_list.append(arts[cont]['data']['title'])
        return recurse(subreddit, hot_list, cont + 1)
    else:
        return(None)
