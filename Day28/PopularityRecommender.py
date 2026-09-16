import pandas as pd

# Movie dataset
movies = pd.DataFrame({
    "Movie": [
        "Inception",
        "Interstellar",
        "Avatar",
        "Titanic",
        "The Dark Knight"
    ],
    "Rating": [
        8.8,
        8.7,
        7.8,
        7.9,
        9.0
    ],
    "Votes": [
        5000,
        4500,
        4200,
        3900,
        6000
    ]
})

# Calculate a simple popularity score
movies["Popularity_Score"] = (
    movies["Rating"] * movies["Votes"]
)

# Sort by popularity
recommendations = movies.sort_values(
    by="Popularity_Score",
    ascending=False
)

print("Popular Movie Recommendations:")
print(
    recommendations[
        ["Movie", "Rating", "Votes"]
    ]
)
