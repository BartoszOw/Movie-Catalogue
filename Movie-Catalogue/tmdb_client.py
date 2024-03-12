import requests
import random

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzZTUwMjVmOGM5YTM5M2NiMTFlNjE5YjE3NGFkN2M4NCIsInN1YiI6IjY1ZjA3ZDdlNjZhN2MzMDE2MmRlODRiZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._pmiP1E1F5JvNbruieSt-BtSZxhtNUvFc23L53KgYPM'
    headers = {
        'Authorization': f'Bearer {api_token}'
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size='w342'):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}{poster_api_path}"

def get_movies(how_many):
    data = get_popular_movies()
    data = random.sample(data['results'], k=how_many)
    return data



