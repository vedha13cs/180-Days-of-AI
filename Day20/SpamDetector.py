from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

print("📧 SPAM MESSAGE DETECTOR")
print("=" * 55)

# Training messages
messages = [
    "Congratulations you won a free prize",
    "Win a free lottery ticket now",
    "You have won a cash reward",
    "Claim your free gift today",
    "Congratulations claim your prize",
    "Get free money now",
    "You won a special reward",
    "Free offer available click now",

    "Can we meet tomorrow",
    "Please send me the assignment",
    "Your class starts at 9 AM",
    "Don't forget the project meeting",
    "Can you call me later",
    "I will reach college at 9",
    "Please share the notes",
    "Let's study together today"
]

# 1 = Spam
# 0 = Not Spam

labels = [
    1, 1, 1, 1,
    1, 1, 1, 1,
    0, 0, 0, 0,
    0, 0, 0, 0
]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    messages,
    labels,
    test_size=0.25,
    random_state=42,
    stratify=labels
)

# Convert text into numerical features
vectorizer = CountVectorizer()

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

print("\n📝 TEXT CONVERTED INTO NUMBERS")

# Create model
model = MultinomialNB()

# Train
model.fit(X_train_vectorized, y_train)

print("🧠 NAIVE BAYES MODEL TRAINED")

# Predictions
predictions = model.predict(X_test_vectorized)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("\n📊 MODEL PERFORMANCE")
print("-" * 35)

print("Accuracy:", round(accuracy * 100, 2), "%")

# Confusion Matrix
print("\n🔲 CONFUSION MATRIX")
print("-" * 35)

print(confusion_matrix(y_test, predictions))

# Classification report
print("\n📋 CLASSIFICATION REPORT")
print("-" * 35)

print(
    classification_report(
        y_test,
        predictions,
        target_names=["Not Spam", "Spam"],
        zero_division=0
    )
)

# Test new messages
new_messages = [
    "Congratulations you won a free gift",
    "Please send me today's class notes",
    "Claim your free cash prize now",
    "Can we meet after college"
]

new_vectors = vectorizer.transform(new_messages)

new_predictions = model.predict(new_vectors)
probabilities = model.predict_proba(new_vectors)

print("\n🔮 NEW MESSAGE PREDICTIONS")
print("-" * 45)

for message, prediction, probability in zip(
    new_messages,
    new_predictions,
    probabilities
):

    result = "SPAM 🚨" if prediction == 1 else "NOT SPAM ✅"

    print(f"\nMessage: {message}")
    print("Prediction:", result)
    print(
        "Spam Probability:",
        round(probability[1] * 100, 2),
        "%"
    )

print("\n" + "=" * 55)
print("✅ DAY 20 COMPLETED!")
print("📧 Spam detector built successfully!")
