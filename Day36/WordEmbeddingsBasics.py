import numpy as np

# Simple example of word vectors
word_vectors = {
    "king": np.array([0.8, 0.9, 0.7]),
    "queen": np.array([0.8, 0.7, 0.9]),
    "man": np.array([0.7, 0.8, 0.6]),
    "woman": np.array([0.7, 0.6, 0.8]),
    "apple": np.array([0.2, 0.3, 0.1])
}

for word, vector in word_vectors.items():
    print(f"{word}: {vector}")

print("\nVector for 'king':")
print(word_vectors["king"])
