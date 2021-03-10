import requests_with_caching
import json


def get_movies_from_tastedive(film):
    baseurl = "https://tastedive.com/api/similar"
    param_f = {}
    param_f["type"] = "movies"
    param_f["limit"] = "5"
    param_f["q"] = film
    reqf = requests_with_caching.get(baseurl, params=param_f)
    filmjs = reqf.json()
    return (filmjs)


def extract_movie_titles(actor_name):
    name = []
    for i in actor_name["Similar"]['Results']:
        name.append(i["Name"])
    return (name)


def get_related_titles(film_name):
    movie_list = []
    for i in film_name:
        ext = extract_movie_titles(get_movies_from_tastedive(i))
        for i in ext:
            if i not in movie_list:
                movie_list.append(i)
    return (movie_list)


def get_movie_data(title):
    baseurl = "http://www.omdbapi.com/"
    film_param = {}
    film_param["t"] = title
    film_param["r"] = "json"
    reqf = requests_with_caching.get(baseurl, params=film_param)
    reqfjson = reqf.json()
    return (reqfjson)


def get_movie_rating(dic):
    rating = 0
    for i in dic["Ratings"]:
        print(i)
        if i["Source"] == "Rotten Tomatoes":
            rating = int(i["Value"][:-1])
    return rating


def get_sorted_recommendations(lst_movies):
    list = get_related_titles(lst_movies)
    dict = {}
    for movie in list:
        rating = get_movie_rating(get_movie_data(movie))
        dict[movie] = rating
    return [movie[0] for movie in sorted(dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]
