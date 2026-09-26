import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

word_vectors = {
    "python": np.array([0.9, 0.8, 0.7]),
    "java": np.array([0.8, 0.7, 0.6]),
    "banana": np.array([0.1, 0.2, 0.3]),
    "apple": np.array([0.2, 0.3, 0.2])
}

word1 = "python"
word2 = "java"

vector1 = word_vectors[word1].reshape(1, -1)
vector2 = word_vectors[word2].reshape(1, -1)

similarity = cosine_similarity(vector1, vector2)[0][0]

print(f"Similarity between '{word1}' and '{word2}':")
print(round(similarity, 2))
