import json
from pprint import pprint


def movie_info(movies, genres):       # movie_info 정의
    results = []                      # value 할당
    genres_dict = {}                  # dict 선언

    for genre in genres:
        genres_dict[genre.get('id')] = genre.get('name') #genres_dict[genre.get('id')]는 genre.get('name')에서 옴(반복문)

    for movie in movies:
        print(movie)
        movie_id = movie.get('id')         # movie_id는 movie의 'id'통해 반환
        genre_ids = movie.get('genre_ids') # 
        genre_names = []

        for genre_id in genre_ids:
            genre_names.append(genres_dict[genre_id])  #genre_names에 genres_dict[genre_id] 추가

        detail = {
            "id": movie_id,
            "title": movie.get('title'),
            "poster_path": movie.get('poster_path'),
            "vote_average": movie.get('vote_average'),
            "overview": movie.get('overview'),
            "genre_names": genre_names,
        }
        results.append(detail)      #results 에 detail 추가
    return results                  #results 반환


if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))   #보기 이쁘게 프린트
