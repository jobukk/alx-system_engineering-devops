import requests
"""
Importing requests module
"""


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of
    subscribers for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'My User Agent 1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        elif response.status_code == 404:
            return 0
        else:
            return 0
    except requests.RequestException:
        return 0
