import requests
from pprint import pprint

def ranking():

    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': 'e83f88f5ecad86f0ce0cb28183447fc0',
        'language': 'ko',
        'region': 'KR',
    }

    response = requests.get(BASE_URL + path, params=params).json()
    results = response.get('results')

    results = sorted(
        results, key=lambda result: result.get('vote_average'), reverse=True
    )
#참고함 ㅠ
    return results[:5]


if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화.
    """
    pprint(ranking())

