from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "I love learning Python and machine learning",
    "Python and machine learning are interesting",
    "I enjoy playing football and cricket"
]

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

similarity = cosine_similarity(tfidf_matrix)

print("Cosine Similarity Matrix:")
print(similarity)

print("\nSimilarity between Document 1 and Document 2:")
print(round(similarity[0][1], 2))

print("\nSimilarity between Document 1 and Document 3:")
print(round(similarity[0][2], 2))
