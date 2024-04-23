
from pytest import MonkeyPatch
from main import app
from unittest.mock import Mock

def test_homepage(monkeypatch: MonkeyPatch):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr('tmdb_client.get_movies', api_mock)

    test_list_type = 'popular'

    with app.test_client() as client: 
        
        response = client.get('/')
        assert response.status_code == 200

        api_mock.assert_called_once_with(8, list_type=test_list_type)
