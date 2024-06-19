from requests import get


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'my-custom-user-agent/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = get(url, headers=user_agent, allow_redirects=False)
        if response.status_code == 200:
            all_data = response.json()
            return all_data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0
