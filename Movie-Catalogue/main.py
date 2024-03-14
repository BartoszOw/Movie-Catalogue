from flask import Flask, render_template, request, redirect, url_for
import tmdb_client

app = Flask(__name__)

@app.context_processor
def utility_processor():

    def tmdb_image_url(path,size):
        return tmdb_client.get_poster_url(path,size)
    
    return {'tmdb_image_url': tmdb_image_url}

LIST_TYPES = [
    {'name': "Now Playing", 'type': "now_playing"},
    {'name': "Top Rated", 'type': "top_rated"},
    {'name': "Upcoming", 'type': "upcoming"},
    {'name': "Popular", 'type': "popular"}
]

@app.route('/')
def homepage():

    selected_list = request.args.get('list_type', 'popular')

    valid_list_types = [lst['type'] for lst in LIST_TYPES]

    if selected_list not in valid_list_types:
        return redirect(url_for('homepage', list_type='popular'))
    
    movies = tmdb_client.get_movies(8, list_type=selected_list)

    return render_template('homepage.html', movies=movies, list=LIST_TYPES, selected_list=selected_list)

@app.route('/movie/<movie_id>')
def movie_details(movie_id):

    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    photo = tmdb_client.get_single_movie_photo(movie_id)

    return render_template('movie_details.html', movie=details, photo=photo, cast=cast)


if __name__ == '__main__':
    app.run(debug=True)