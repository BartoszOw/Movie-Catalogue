import requests
import random



API_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzZTUwMjVmOGM5YTM5M2NiMTFlNjE5YjE3NGFkN2M4NCIsInN1YiI6IjY1ZjA3ZDdlNjZhN2MzMDE2MmRlODRiZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._pmiP1E1F5JvNbruieSt-BtSZxhtNUvFc23L53KgYPM'

#def get_popular_movies():
#    endpoint = "https://api.themoviedb.org/3/movie/popular"
#    headers = {
#        'Authorization': f'Bearer {API_TOKEN}'
#
#    response = requests.get(endpoint, headers=headers)
#    return response.json()

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_poster_url(poster_api_path, size='w342'):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}{poster_api_path}"

def get_movies(how_many, list_type='popular'):
    data = get_movies_list(list_type)
    data = random.sample(data['results'], k=how_many)
    return data

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()['cast']


def get_single_movie_photo(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }
    response = requests.get(endpoint, headers=headers)
    return random.sample(response.json()['backdrops'], k=1)
