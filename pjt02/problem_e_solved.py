import requests
from pprint import pprint


def credits(title):
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

    # https://developers.themoviedb.org/3/movies/get-movie-credits

    path = f'/movie/{movie_id}/credits'
    params = {
        'api_key': 'e83f88f5ecad86f0ce0cb28183447fc0',
        'language': 'ko',
        'region': 'KR',
    }


    response = requests.get(BASE_URL + path, params=params).json()

    casts = response.get('cast')
    crews = response.get('crew')

    result = {'cast': [], 'crew': []}

    for cast in casts:
        if cast.get('cast_id') < 10:
            result['cast'].append(cast.get('name'))

    for crew in crews:
        if crew.get('department') == 'Directing':
            result['crew'].append(crew.get('name'))

    return result


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록(cast)과 제작진(crew).
    영화 id검색에 실패할 경우 None.
    """
    pprint(credits('기생충'))
    # => {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # => None
