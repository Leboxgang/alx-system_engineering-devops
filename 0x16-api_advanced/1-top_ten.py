#!/usr/bin/python3

import requests as r


def top_ten(subreddit):
    """Print top 10 post given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
 }
    param = {
        "limit": 10
    }
    response = r.get(url, headers=headers, params=param, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(top.get("data").get("title")) for top in results.get("children")]
