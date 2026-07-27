import sqlite3

# ------------------ Database ------------------

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Movies(
    MovieID INTEGER PRIMARY KEY,
    Title TEXT,
    Genre TEXT,
    Rating REAL,
    WatchCount INTEGER
)
""")

# Delete old records (Optional)
cursor.execute("DELETE FROM Movies")

# ------------------ Dynamic Input ------------------

n = int(input("Enter number of movies: "))

for i in range(n):
    print("\nEnter Details of Movie", i + 1)

    mid = int(input("Movie ID: "))
    title = input("Movie Title: ")
    genre = input("Genre: ")
    rating = float(input("Rating: "))
    watch = int(input("Watch Count: "))

    cursor.execute(
        "INSERT INTO Movies VALUES (?,?,?,?,?)",
        (mid, title, genre, rating, watch)
    )

conn.commit()

# ------------------ Fetch Movies ------------------

cursor.execute("SELECT * FROM Movies")
movies = cursor.fetchall()

# ------------------ Sort by Rating ------------------

movies.sort(key=lambda x: x[3])

print("\nMovies Sorted by Rating\n")

for movie in movies:
    print(movie)

# ------------------ Binary Search ------------------

movies_by_id = sorted(movies, key=lambda x: x[0])

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid][0] == key:
            return arr[mid]
        elif arr[mid][0] < key:
            low = mid + 1
        else:
            high = mid - 1

    return None

search_id = int(input("\nEnter Movie ID to Search: "))

result = binary_search(movies_by_id, search_id)

if result:
    print("\nMovie Found")
    print("Movie ID    :", result[0])
    print("Title       :", result[1])
    print("Genre       :", result[2])
    print("Rating      :", result[3])
    print("Watch Count :", result[4])
else:
    print("Movie Not Found")

# ------------------ Top 10 Highest Rated ------------------

movies_desc = sorted(movies, key=lambda x: x[3], reverse=True)

print("\nTop Highest Rated Movies\n")

count = min(10, len(movies_desc))

for i in range(count):
    print(movies_desc[i])

# ------------------ Most Watched Movie in Each Genre ------------------

genre_movies = {}

for movie in movies:
    genre = movie[2]

    if genre not in genre_movies:
        genre_movies[genre] = movie
    elif movie[4] > genre_movies[genre][4]:
        genre_movies[genre] = movie

print("\nMost Watched Movie in Every Genre\n")

for genre, movie in genre_movies.items():
    print("Genre :", genre)
    print("Movie :", movie[1])
    print("Watch Count :", movie[4])
    print()

conn.close()