import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

print("🧠 NAIVE BAYES CLASSIFIER")
print("=" * 50)

# Features:
# [Study Hours, Attendance]

X = np.array([
    [1, 60],
    [2, 65],
    [2.5, 68],
    [3, 70],
    [3.5, 72],
    [4, 75],
    [5, 80],
    [5.5, 82],
    [6, 85],
    [7, 88],
    [8, 90],
    [9, 95],
    [10, 97]
])

# 0 = Fail
# 1 = Pass

y = np.array([
    0, 0, 0, 0,
    0, 1, 1, 1,
    1, 1, 1, 1,
    1
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
model = GaussianNB()

# Train
model.fit(X_train, y_train)

print("\n🧠 MODEL TRAINED")

# Predictions
predictions = model.predict(X_test)

print("\n🎯 TEST PREDICTIONS")
print("-" * 35)

for actual, predicted in zip(y_test, predictions):

    actual_result = "PASS" if actual == 1 else "FAIL"
    predicted_result = "PASS" if predicted == 1 else "FAIL"

    print(
        f"Actual: {actual_result} | "
        f"Predicted: {predicted_result}"
    )

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("\n📊 MODEL PERFORMANCE")
print("-" * 35)

print("Accuracy:", round(accuracy * 100, 2), "%")

# Confusion Matrix
print("\n🔲 CONFUSION MATRIX")
print("-" * 35)

print(confusion_matrix(y_test, predictions))

# Classification Report
print("\n📋 CLASSIFICATION REPORT")
print("-" * 35)

print(
    classification_report(
        y_test,
        predictions,
        target_names=["Fail", "Pass"],
        zero_division=0
    )
)

# New student
new_student = np.array([
    [6.5, 85]
])

prediction = model.predict(new_student)[0]
probability = model.predict_proba(new_student)[0]

result = "PASS 🎉" if prediction == 1 else "FAIL 📚"

print("\n🔮 NEW STUDENT")
print("-" * 35)

print("Study Hours:", new_student[0][0])
print("Attendance:", new_student[0][1], "%")

print(
    "Fail Probability:",
    round(probability[0] * 100, 2),
    "%"
)

print(
    "Pass Probability:",
    round(probability[1] * 100, 2),
    "%"
)

print("Prediction:", result)

print("\n" + "=" * 50)
print("✅ DAY 20 COMPLETED!")
