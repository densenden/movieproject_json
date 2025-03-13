import random
import movie_storage
import json

def list_movies():
    with open("data.json", "r") as movie_database:
        movie_database = json.load(movie_database)
        print(f"{len(movie_database)} movies in total")
        for title, info in movie_database.items():
            print(f"{title} ({info['year']}): {info['rating']}")

def stats():
    ratings = []
    with open("data.json", "r") as movie_database:
        movie_database = json.load(movie_database)
        for title, info in movie_database.items():
            ratings.append(info["rating"])

    avg_rating = round(sum(ratings) / len(movie_database), 1)
    print(f"Average Rating of {len(movie_database)} Movies: {avg_rating}")

    best_rating = max(ratings)
    worst_rating = min(ratings)

    best_movies = [title for title, info in movie_database.items() if info["rating"] == best_rating]
    worst_movies = [title for title, info in movie_database.items() if info["rating"] == worst_rating]
    average_movies = [title for title, info in movie_database.items() if info["rating"] == avg_rating]

    for title in average_movies:
        print(f"Average Movie: {title}")

    for title in best_movies:
        print(f"Best Movie: {title} ({best_rating})")

    for title in worst_movies:
        print(f"Worst Movie: {title} ({worst_rating})")

def random_movie():
    with open("data.json", "r") as movie_database:
        movie_database = json.load(movie_database)
        all_titles = list(movie_database.keys())
        title = random.choice(all_titles)
        print(f"A Random Movie: {title} (Rating: {movie_database[title]['rating']})")

def search_movie():
    try:
        with open("data.json", "r") as movie_file:
            movie_database = json.load(movie_file)

        query = input("Enter part of a movie name: ").lower()

        found_movies = [
            f"{movie_name} ({data['year']}): {data['rating']}"
            for movie_name, data in movie_database.items()
            if query in movie_name.lower()
        ]

        if found_movies:
            print("\nMatching Movies:")
            print("\n".join(found_movies))
        else:
            print("No movies found matching your query.")
    except FileNotFoundError:
        print("Error: The database file does not exist.")
    except json.JSONDecodeError:
        print("Error: The database file is not valid JSON.")

def movies_sorted_by_rating():
    try:
        with open("data.json", "r") as movie_file:
            movie_database = json.load(movie_file)

        sorted_movies = sorted(movie_database.items(), key=lambda item: item[1]["rating"], reverse=True)

        print("Movies sorted by rating:")
        for title, info in sorted_movies:
            print(f"{title} ({info['rating']})")
    except FileNotFoundError:
        print("Error: The database file does not exist.")
    except json.JSONDecodeError:
        print("Error: The database file is not valid JSON.")

def movies_sorted_by_year():
    try:
        with open("data.json", "r") as movie_file:
            movie_database = json.load(movie_file)

        sorted_movies_year = sorted(movie_database.items(), key=lambda item: item[1]["year"], reverse=True)

        print("Movies sorted by year:")
        for title, info in sorted_movies_year:
            print(f"{title} ({info['year']})")
    except FileNotFoundError:
        print("Error: The database file does not exist.")
    except json.JSONDecodeError:
        print("Error: The database file is not valid JSON.")

def filter_movies():
    min_rating = input("Enter the minimum rating (1-10): ").strip()
    start_year = input("Enter the start year: ").strip()
    end_year = input("Enter the end year: ").strip()

    if not min_rating or not start_year or not end_year:
        print("Error: All fields are required.")
        return

    try:
        min_rating = float(min_rating)
        start_year = int(start_year)
        end_year = int(end_year)
    except ValueError:
        print("Error: Invalid input. Rating must be a number (1-10), and years must be integers.")
        return

    filtered_movies = movie_storage.filter_movies(min_rating, start_year, end_year)

    if filtered_movies:
        print(f"\nMovies matching your criteria ({len(filtered_movies)} found):")
        for title, info in filtered_movies.items():
            print(f"{title} ({info['year']}): {info['rating']}")
    else:
        print("No movies found matching your criteria.")

def add_movie():
    title = input("Enter movie name: ").strip()
    rating = input("Enter movie rating (1-10): ").strip()
    year = input("Enter year of release: ").strip()

    if not title or not rating or not year:
        print("Error: All fields are required.")
        return

    try:
        rating = float(rating)
        year = int(year)
    except ValueError:
        print("Error: Invalid input. Rating must be a number (1-10), and year must be an integer.")
        return

    if not (1 <= rating <= 10):
        print("Error: Rating must be between 1 and 10.")
        return

    movie_storage.add_movie(title, rating, year)
    print(f"Movie '{title}' successfully added to the database!")

def delete_movie():
    title = input("Enter movie name to delete: ").strip()
    if movie_storage.delete_movie(title):
        print(f"Movie '{title}' was successfully deleted.")
    else:
        print("Error: Movie not found.")

def update_movie():
    title = input("Enter movie name to update: ").strip()
    new_rating = input("Enter new rating (1-10): ").strip()

    if not title or not new_rating:
        print("Error: All fields are required.")
        return

    try:
        new_rating = float(new_rating)
    except ValueError:
        print("Error: Invalid input. Rating must be a number (1-10).")
        return

    if not (1 <= new_rating <= 10):
        print("Error: Rating must be between 1 and 10.")
        return

    if movie_storage.update_movie(title, new_rating):
        print(f"Movie '{title}' updated successfully with a new rating: {new_rating}")
    else:
        print("Error: Movie not found.")

menu_options = {
    0: exit,
    1: list_movies,
    2: add_movie,
    3: delete_movie,
    4: update_movie,
    5: stats,
    6: random_movie,
    7: search_movie,
    8: movies_sorted_by_rating,
    9: movies_sorted_by_year,
    10: filter_movies
}

def main():
    while True:
        user_input = input(f"""
            ╔══════════════════════════════════════════╗
            ║      PLEASE ENTER A MENU OPTION (0-10)   ║
            ╠══════════════════════════════════════════╣
            ║   0: Exit                                ║
            ║   1: List all movies alphabetically      ║
            ║   2: Add movie                           ║
            ║   3: Delete movie                        ║
            ║   4: Update movie rating                 ║
            ║   5: Movie database stats                ║
            ║   6: Select random movie                 ║
            ║   7: Search movie                        ║
            ║   8: List movies sorted by rating        ║
            ║   9: List movies sorted by year          ║
            ║  10: Filter movies                       ║
            ╚══════════════════════════════════════════╝
            >>> """)

        if not user_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        option = int(user_input)

        if option == 0:
            print("Exiting...")
            break

        if option in menu_options:
            menu_options[option]()
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()