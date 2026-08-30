import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

print("🎓 STUDENT PASS/FAIL MODEL")
print("=" * 50)

# Features:
# [Study Hours, Attendance %, Previous Marks]

X = np.array([
    [2, 65, 45],
    [3, 70, 50],
    [2.5, 68, 48],
    [4, 72, 55],
    [5, 80, 62],
    [4.5, 78, 60],
    [6, 85, 70],
    [7, 88, 75],
    [5.5, 82, 68],
    [8, 90, 80],
    [9, 92, 85],
    [7.5, 87, 78],
    [3.5, 60, 42],
    [2, 55, 38],
    [6.5, 84, 73],
    [8.5, 91, 82]
])

# 0 = Fail
# 1 = Pass

y = np.array([
    0, 0, 0, 0,
    1, 1, 1, 1,
    1, 1, 1, 1,
    0, 0, 1, 1
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
model = LogisticRegression(max_iter=1000)

# Train
model.fit(X_train, y_train)

print("\n🧠 MODEL TRAINED")

# Predictions
predictions = model.predict(X_test)

# Metrics
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)

print("\n📊 MODEL PERFORMANCE")
print("-" * 35)

print("Accuracy :", round(accuracy * 100, 2), "%")
print("Precision:", round(precision, 3))
print("Recall   :", round(recall, 3))
print("F1 Score :", round(f1, 3))

print("\n🔲 CONFUSION MATRIX")
print(confusion_matrix(y_test, predictions))

# New student
new_student = np.array([
    [6, 85, 72]
])

prediction = model.predict(new_student)[0]
probability = model.predict_proba(new_student)[0][1]

result = "PASS 🎉" if prediction == 1 else "FAIL 📚"

print("\n🔮 NEW STUDENT PREDICTION")
print("-" * 35)

print("Study Hours:", new_student[0][0])
print("Attendance:", new_student[0][1], "%")
print("Previous Marks:", new_student[0][2])

print(
    "Pass Probability:",
    round(probability * 100, 2),
    "%"
)

print("Prediction:", result)

print("\n" + "=" * 50)
print("✅ DAY 15 COMPLETED!")
print("🎯 Model evaluated successfully!")
