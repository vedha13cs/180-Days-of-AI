from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

texts = [
    "I love learning Python",
    "Machine learning is amazing",
    "I enjoy artificial intelligence",
    "I hate this experience",
    "This is a terrible mistake",
    "I am disappointed with the service"
]

labels = [
    "Positive",
    "Positive",
    "Positive",
    "Negative",
    "Negative",
    "Negative"
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

new_texts = [
    "I enjoy learning machine learning",
    "This is a terrible experience"
]

new_X = vectorizer.transform(new_texts)

predictions = model.predict(new_X)

for text, prediction in zip(new_texts, predictions):
    print("Text:", text)
    print("Prediction:", prediction)
    print("-" * 50)
