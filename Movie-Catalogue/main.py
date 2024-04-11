from flask import Flask, render_template, request, redirect, url_for, flash
import tmdb_client
import datetime
import envs


app = Flask(__name__)
app.secret_key = b'DAScDWADSdFa'


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

FAVORITES = set()

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


@app.route('/search')
def search():
    search_query = request.args.get('search_res', '')
    if search_query:
        movies = tmdb_client.search(search_query=search_query)
    else:
        movies = []
    return render_template('search.html', movies=movies, search_query=search_query)

@app.route('/today')
def today():
    movies = tmdb_client.get_airing_today()
    today = datetime.date.today()
    return render_template('today.html', movies=movies, today=today)

@app.route('/favorites/add', methods=['POST'])
def add_to_favorites():
    data = request.form
    movie_id = data.get('movie_id')
    movie_title = data.get('movie_title')
    if movie_id:
        FAVORITES.add(movie_id)
        flash(f"{movie_title} Added to your favorites")
    return redirect(url_for('homepage'))

@app.route('/favorites')
def show_favorites():
    if FAVORITES:
        movies = []
        for movie_id in FAVORITES:
            movie_details = tmdb_client.get_single_movie(movie_id)
            movies.append(movie_details)
    else:
        movies = []
    return render_template('homepage.html', movies=movies)
    
if __name__ == '__main__':
    app.run(debug=True)