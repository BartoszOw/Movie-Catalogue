
# Movie Catalogue
## Overview
Movie Catalogue is a web application built with Flask that allows users to explore a vast collection of movies sourced from the TMDB (The Movie Database) API. Users can discover popular, top-rated, upcoming, and currently playing movies, search for specific titles, view movie details including cast information and images, and add their favorite movies to a personal favorites list.

## Features
- Browse movies by various categories such as now playing, top rated, upcoming, and popular.
- Search for movies by title.
- View detailed information about a specific movie, including cast members and images.
- Add favorite movies to a personal favorites list.
## Technologies Used
- ``Flask:`` Python web framework used for building the backend server.
- ``TMDB API:`` Source of movie data, providing information about movie details, cast, images, and more.
- ``HTML/CSS:`` Frontend templates and styling.
- ``Bootstrap:`` Frontend framework for responsive design.
- ``Python-dotenv:`` Library for loading environment variables from a .env file.
- `Requests:` HTTP library for making API requests.
- `Jinja2:` Template engine for rendering dynamic content in HTML templates.
- `Unittest:` Python testing framework for writing and running unit tests.
## Usage
Clone the repository:

```
git clone https://github.com/your_username/movie-catalogue.git
```
Install dependencies:

```
pip install -r requirements.txt
```
Set up environment variables:

Create a `.env` file in the project root directory and add your TMDB API token:

```
TMDB_API_TOKEN=your_tmdb_api_token_here
```
Run the Flask application:

```
python main.py
```
Access the application in your web browser at http://localhost:5000.

## Testing
This project includes unit tests to ensure its functionality. To run the tests, execute the following command:

```
python -m unittest discover
```

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

