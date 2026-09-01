import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("🌲 RANDOM FOREST CLASSIFIER")
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
    [10, 96]
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

# Create Random Forest
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=4,
    random_state=42
)

# Train
model.fit(X_train, y_train)

print("\n🌲 RANDOM FOREST TRAINED")
print("Number of Trees:", model.n_estimators)

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

print("\n📊 MODEL ACCURACY")
print("-" * 35)

print("Accuracy:", round(accuracy * 100, 2), "%")

# New prediction
new_student = np.array([[6, 85]])

prediction = model.predict(new_student)[0]
probability = model.predict_proba(new_student)[0]

result = "PASS 🎉" if prediction == 1 else "FAIL 📚"

print("\n🔮 NEW PREDICTION")
print("-" * 35)

print("Study Hours:", new_student[0][0])
print("Attendance:", new_student[0][1], "%")

print(
    "Pass Probability:",
    round(probability[1] * 100, 2),
    "%"
)

print("Prediction:", result)

print("\n" + "=" * 50)
print("✅ DAY 17 COMPLETED!")
