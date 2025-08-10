#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Prints the titles of the 10 hottest posts on a given subreddit."""

    if subreddit is None:
        return hot_list
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    params = {
        "limit": 100,
        "after": after
    }

    response = requests.get(
            url, headers=headers, params=params,
            allow_redirects=False, 
    timeout=60)
    if response.status_code == 404:
        return None
    results = response.json().get("data", {})
    if results is None or not results.get("children"):
        return hot_list

    after = results.get("after")
    for c in results.get("children", []):
        hot_list.append(c.get("data").get("title"))

    if (after is not None):
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
