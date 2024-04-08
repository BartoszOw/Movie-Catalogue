import tmdb_client



def test_get_poster_url_uses_default_size():
    poster_api_path = 'some-poster-path'
    expected_default_size = 'w342'

    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)

    assert poster_url == "https://image.tmdb.org/t/p/w342/some-poster-path"


def test_get_movies_list_type_popular():
    movies_list = tmdb_client.get_movies_list(list_type='popular')
    assert movies_list is not None