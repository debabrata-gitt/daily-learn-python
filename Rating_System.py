movies = {
    "Avengers": 9,
    "Avatar": 8,
    "Titanic": 9,
    "Inception": 10
}

movie = max(movies, key=movies.get)

print("⭐ Highest rated movie:", movie)
print("Rating:", movies[movie], "/10")