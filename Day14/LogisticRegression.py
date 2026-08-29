import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

print("🎯 LOGISTIC REGRESSION")
print("=" * 45)

# Study hours
X = np.array([
    [1], [2], [2.5], [3], [3.5],
    [4], [5], [5.5], [6], [7],
    [7.5], [8], [9], [10]
])

# 0 = Fail, 1 = Pass
y = np.array([
    0, 0, 0, 0, 0,
    0, 1, 1, 1, 1,
    1, 1, 1, 1
])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Create model
model = LogisticRegression()

# Train
model.fit(X_train, y_train)

print("\n🧠 MODEL TRAINED")

# Predictions
predictions = model.predict(X_test)

# Probabilities
probabilities = model.predict_proba(X_test)

print("\n🎯 TEST PREDICTIONS")
print("-" * 35)

for hours, actual, predicted, probability in zip(
    X_test.flatten(),
    y_test,
    predictions,
    probabilities[:, 1]
):
    result = "PASS" if predicted == 1 else "FAIL"

    print(
        f"{hours} hours → "
        f"Actual: {actual} | "
        f"Prediction: {result} | "
        f"Pass Probability: {probability:.2f}"
    )

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("\n📊 MODEL EVALUATION")
print("-" * 30)

print("Accuracy:", round(accuracy * 100, 2), "%")

print("\n🔲 CONFUSION MATRIX")
print(confusion_matrix(y_test, predictions))

# New prediction
new_student = np.array([[6.5]])

prediction = model.predict(new_student)[0]
probability = model.predict_proba(new_student)[0][1]

result = "PASS" if prediction == 1 else "FAIL"

print("\n🔮 NEW PREDICTION")
print("-" * 30)

print("Study Hours:", new_student[0][0])
print("Pass Probability:", round(probability * 100, 2), "%")
print("Prediction:", result)

print("\n" + "=" * 45)
print("✅ DAY 14 COMPLETED!")
