import tmdb_client
from unittest.mock import Mock

def test_get_poster_url_uses_default_size():
    poster_api_path = 'some-poster-path'
    expected_default_size = 'w342'

    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)

    assert poster_url == "https://image.tmdb.org/t/p/w342/some-poster-path"


def test_get_movies_list_type_popular():
    movies_list = tmdb_client.get_movies_list(list_type='popular')
    assert movies_list is not None


# Mock i monkeypatch


def test_get_movies_list(monkeypatch):
    mock_movies_list = ["Movie 1", "Movie 2"]

    request_mock = Mock()
    response = request_mock.return_value
    response.json.return_value = mock_movies_list
    monkeypatch.setattr('tmdb_client.requests.get', request_mock)

    movies_list = tmdb_client.get_movies_list(list_type='popular')
    assert movies_list == mock_movies_list

def test_get_single_movie(monkeypatch):

    request_mock = Mock()
    request_mock.return_value = '333' 
    monkeypatch.setattr('tmdb_client.get_single_movie', request_mock)
    res = tmdb_client.get_single_movie()
    assert res == '333'

def test_get_single_movie_photo(monkeypatch):

    request_mock = Mock()
    request_mock.return_value = '111'
    monkeypatch.setattr('tmdb_client.get_single_movie_photo', request_mock)
    res = tmdb_client.get_single_movie_photo()
    assert res == '111'


def test_get_single_movie_cast(monkeypatch):
    expected_cast_list = [{'name': "Al Pacino"},{'name': "Steven Bauer"}]
    request_mock = Mock()
    request_mock.return_value = expected_cast_list
    monkeypatch.setattr('tmdb_client.get_single_movie_cast', request_mock)
    movie_cast = tmdb_client.get_single_movie_cast(movie_id='111')
    assert movie_cast == expected_cast_list

def test_search(monkeypatch):
    
    request_mock = Mock()
    request_mock.return_value = 'Migration'
    monkeypatch.setattr('tmdb_client.search', request_mock)
    res = tmdb_client.search(request_mock.return_value)
    assert res == 'Migration'

