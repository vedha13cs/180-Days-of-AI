from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "I love machine learning",
    "I love artificial intelligence",
    "Machine learning is powerful"
]

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

print("Vocabulary:")
print(vectorizer.get_feature_names_out())

print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())
