from sklearn.feature_extraction.text import CountVectorizer

sentences = [
    "I love artificial intelligence",
    "I love machine learning",
    "Artificial intelligence is powerful"
]

vectorizer = CountVectorizer()

matrix = vectorizer.fit_transform(sentences)

print("Vocabulary:")
print(vectorizer.get_feature_names_out())

print("\nBag of Words Matrix:")
print(matrix.toarray())
