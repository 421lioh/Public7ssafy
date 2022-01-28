import requests
from pprint import pprint


def recommendation(title):

    # https://developers.themoviedb.org/3/search/search-movies
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': 'e83f88f5ecad86f0ce0cb28183447fc0',
        'language': 'ko',
        'region': 'KR',
        'query': title,
    }

    response = requests.get(BASE_URL + path, params=params).json()
    results = response.get('results')

    if len(results):
        movie_id = results[0].get('id')
    else:
        return None

    # https://developers.themoviedb.org/3/movies/get-movie-recommendation
    path = f'/movie/{movie_id}/recommendations'
    params = {
        'api_key': 'e83f88f5ecad86f0ce0cb28183447fc0',
        'language': 'ko',
    }

    response = requests.get(BASE_URL + path, params=params).json()
    results = response.get('results')

    movies = []
    for result in results:
        movies.append(result.get('title'))

    return movies


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록 구성.
    추천 영화가 없을 경우 [].
    영화 id검색에 실패할 경우 None.
    """
    pprint(recommendation('기생충'))
    # ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
    pprint(recommendation('그래비티'))
    # []  => 추천 영화 없음
    pprint(recommendation('검색할 수 없는 영화'))
    # => None

