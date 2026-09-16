import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Movie dataset
movies = pd.DataFrame({
    "Title": [
        "Inception",
        "Interstellar",
        "The Martian",
        "Titanic",
        "The Notebook",
        "Avatar"
    ],

    "Description": [
        "science fiction thriller dream technology",
        "science fiction space adventure technology",
        "science fiction space survival adventure",
        "romance drama ocean love",
        "romance drama relationship love",
        "science fiction adventure alien technology"
    ]
})


# Convert text into numerical vectors
vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(
    movies["Description"]
)


# Calculate similarity
similarity = cosine_similarity(
    tfidf_matrix
)


# Create title-to-index mapping
indices = pd.Series(
    movies.index,
    index=movies["Title"]
)


def recommend_movie(title, number=3):

    index = indices[title]

    # Similarity scores for selected movie
    scores = list(
        enumerate(similarity[index])
    )

    # Sort from highest similarity
    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    # Remove the selected movie itself
    scores = scores[1:number + 1]

    recommended_indices = [
        item[0]
        for item in scores
    ]

    return movies.iloc[
        recommended_indices
    ]["Title"]


# Example recommendation
movie = "Interstellar"

print(f"Recommendations for: {movie}")

recommendations = recommend_movie(movie)

for item in recommendations:
    print("🎬", item)
