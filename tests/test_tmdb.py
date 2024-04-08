

import tmdb_client





def test_get_poster_url_uses_default_size():
    poster_api_path = 'some-poster-path'
    expected_default_size = 'w342'

    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)

    assert expected_default_size in poster_url