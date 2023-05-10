import requests


def request_api_data(password):
    url = 'https://api.pwnedpasswords.com/range/' + password
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check API and try again')
    return res
