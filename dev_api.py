import requests


apikey = 'enter-your-api-key-here'

headers = {
    "api-key": apikey
}

def user_article():
    url = 'https://dev.to/api/articles/me/all'

    parameters = {
        "per_page": 500
    }
    response = requests.get(url, headers=headers, params=parameters)
    return response


def feed():
    url = 'https://dev.to/api/articles'

    parameters = {
        'per_page': 30
    }

    response = requests.get(url, headers=headers, params=parameters)
    return response
