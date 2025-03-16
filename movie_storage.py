import json

JSON_FILENAME = "data.json"

def load_movies():
    """
    Load the movie database from a file.
    """
    try:
        with open(JSON_FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_movies(movie_database):
    """
    Save the movie database to a file.
    """
    with open(JSON_FILENAME, "w", encoding="utf-8") as f:
        json.dump(movie_database, f, indent=4)


def add_movie(title, rating, year):
    """
    Add a movie to the database.
    """
    movie_database = load_movies()
    if title in movie_database:
        print(f"Error: Movie '{title}' already exists.")
        return False
    movie_database[title] = {"rating": rating, "year": year}
    save_movies(movie_database)
    return True


def delete_movie(title):
    """
    Delete a movie from the database.
    """
    movie_database = load_movies()
    if title in movie_database:
        del movie_database[title]
        save_movies(movie_database)
        return True
    return False


def update_movie(title, new_rating):
    """
    Update the rating of a movie in the database.
    """
    movie_database = load_movies()
    if title in movie_database:
        movie_database[title]["rating"] = new_rating
        save_movies(movie_database)
        return True
    return False


def list_movies():
    """
    List all movies from the database.
    """
    return load_movies()


def filter_movies(min_rating=None, start_year=None, end_year=None):
    """
    Filter movies by rating and year range.
    """
    movie_database = load_movies()
    return {
        title: info
        for title, info in movie_database.items()
        if (min_rating is None or info["rating"] >= min_rating) and
           (start_year is None or info["year"] >= start_year) and
           (end_year is None or info["year"] <= end_year)
    }