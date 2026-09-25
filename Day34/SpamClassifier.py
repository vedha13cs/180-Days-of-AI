from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

messages = [
    "Congratulations! You won a free prize",
    "Claim your free gift now",
    "You have won a lottery",
    "Win money by clicking this link",
    "Can we meet tomorrow?",
    "Please send me the project report",
    "Are you coming to college today?",
    "Let's have lunch together"
]

labels = [
    "Spam",
    "Spam",
    "Spam",
    "Spam",
    "Normal",
    "Normal",
    "Normal",
    "Normal"
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(messages)

model = MultinomialNB()
model.fit(X, labels)

new_messages = [
    "Congratulations you won a free gift",
    "Please send me your assignment"
]

new_X = vectorizer.transform(new_messages)

predictions = model.predict(new_X)

for message, prediction in zip(new_messages, predictions):
    print("Message:", message)
    print("Prediction:", prediction)
    print("-" * 50)
