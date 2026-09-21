from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "I love Python",
    "I love AI",
    "Python is powerful"
]

vectorizer = CountVectorizer()

bow_matrix = vectorizer.fit_transform(documents)

print("Vocabulary:")
print(vectorizer.get_feature_names_out())

print("\nBag of Words Matrix:")
print(bow_matrix.toarray())
