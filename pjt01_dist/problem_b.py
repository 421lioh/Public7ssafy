import json
from pprint import pprint


def movie_info(movie, genres):   # movie_info 정의
    genres_dict = {}             #딕셔너리 생성

    for genre in genres:          #반복문 사용
        genres_dict[genre.get('id')] = genre.get('name')  #genres_dict[genre.get('id')]는 genre.get('name')에서 옴

    movie_id = movie.get('id')           #movie에 있는 id로 받아옴
    genre_ids = movie.get('genre_ids')   #""
    genre_names = []                     #키에 대한 value 할당(?)

    for genre_id in genre_ids:
        genre_names.append(genres_dict[genre_id])  #genre_names에 genres_dict[genre_id] 추가

    detail = {                     #movie에 있는 데이터 중 가져와서 출력할 deatil들 가져옴
        "id": movie_id,
        "title": movie.get('title'),
        "poster_path": movie.get('poster_path'),
        "vote_average": movie.get('vote_average'),
        "overview": movie.get('overview'),
        "genre_names": genre_names,
    }

    return detail                 #detail 반환


if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))  #보기 이쁘게 프린트
