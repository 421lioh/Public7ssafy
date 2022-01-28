import requests
from pprint import pprint

def vote_average_movies():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': 'e83f88f5ecad86f0ce0cb28183447fc0',
        'language': 'ko',
        'region': 'KR'
    }

    response = requests.get(BASE_URL + path, params=params).json()
    results = response.get('results')

    vamo8 = []
    for result in results:
        if result.get('vote_average') >= 8:
            vamo8.append(result)

    return vamo8

if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    pprint(vote_average_movies())