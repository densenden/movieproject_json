import json

def load_movies():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_movies(movie_database):
    with open("data.json", "w") as f:
        json.dump(movie_database, f, indent=4)

def add_movie(title, rating, year):
    movie_database = load_movies()
    movie_database[title] = {"rating": rating, "year": year}
    save_movies(movie_database)

def delete_movie(title):
    movie_database = load_movies()
    if title in movie_database:
        del movie_database[title]
        save_movies(movie_database)
        return True
    return False

def update_movie(title, new_rating):
    movie_database = load_movies()
    if title in movie_database:
        movie_database[title]["rating"] = new_rating
        save_movies(movie_database)
        return True
    return False

def list_movies():
    return load_movies()

def filter_movies(min_rating, start_year, end_year):
    movie_database = load_movies()
    return {
        title: info
        for title, info in movie_database.items()
        if info["rating"] >= min_rating and start_year <= info["year"] <= end_year
    }