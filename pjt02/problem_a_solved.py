import requests


def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '7108d7a0290beb4c2d99634b041130ba',
        'language': 'ko',
        'region': 'KR',
    }

    response = requests.get(BASE_URL + path, params=params).json()
    results = response.get('results')

    return len(results)


if __name__ == '__main__':
    """
    popular 영화목록의 개수 출력.
    """
    print(popular_count())
    # => 20