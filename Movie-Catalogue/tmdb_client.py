import requests
import random
import os


API_TOKEN = os.environ.get("TMDB_API_TOKEN", "")


def make_tmdb_request(endpoint):
    headers = {'Authorization': f'Bearer {API_TOKEN}'}
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    return make_tmdb_request(endpoint)

def get_poster_url(poster_api_path, size='w342'):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type='popular'):
    data = get_movies_list(list_type)
    movies = random.sample(data['results'], k=how_many)
    return movies

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    return make_tmdb_request(endpoint)

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    response = make_tmdb_request(endpoint)
    return response['cast']

def get_single_movie_photo(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    response = make_tmdb_request(endpoint)
    backdrops = response.get('backdrops', [])
    if backdrops:
        return random.sample(backdrops, k=min(len(backdrops), 1))
    else:
        return []


def search(search_query):
    base_url = 'https://api.themoviedb.org/3/'
    endpoint = f'{base_url}search/movie?query={search_query}'
    response = make_tmdb_request(endpoint)
    return response['results']

def get_airing_today():
    endpoint = 'https://api.themoviedb.org/3/tv/airing_today'
    response = make_tmdb_request(endpoint)
    return response['results']


