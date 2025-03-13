import json

def storage_load_movies():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def storage_save_movies(movie_database):
    with open("data.json", "w") as f:
        json.dump(movie_database, f, indent=4)

def storage_add_movie(title, rating, year):
    movie_database = storage_load_movies()
    movie_database[title] = {"rating": rating, "year": year}
    storage_save_movies(movie_database)

def storage_delete_movie(title):
    movie_database = storage_load_movies()
    if title in movie_database:
        del movie_database[title]
        storage_save_movies(movie_database)
        return True
    return False

def storage_update_movie(title, new_rating):
    movie_database = storage_load_movies()
    if title in movie_database:
        movie_database[title]["rating"] = new_rating
        storage_save_movies(movie_database)
        return True
    return False

def storage_list_movies():
    return storage_load_movies()

def storage_filter_movies(min_rating, start_year, end_year):
    movie_database = storage_load_movies()
    return {
        title: info
        for title, info in movie_database.items()
        if info["rating"] >= min_rating and start_year <= info["year"] <= end_year
    }