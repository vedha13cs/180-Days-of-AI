import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

print("🎓 STUDENT PERFORMANCE DECISION TREE")
print("=" * 55)

# Features:
# [Study Hours, Attendance %, Previous Marks]

X = np.array([
    [2, 60, 40],
    [3, 65, 45],
    [2.5, 68, 48],
    [4, 70, 52],
    [4.5, 75, 58],
    [5, 78, 62],
    [6, 80, 68],
    [7, 85, 72],
    [5.5, 82, 65],
    [8, 88, 78],
    [9, 92, 85],
    [7.5, 90, 80],
    [3.5, 62, 43],
    [2, 55, 38],
    [6.5, 84, 74],
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

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Create model
model = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

print("\n🌳 DECISION TREE TRAINED!")

# Predictions
predictions = model.predict(X_test)

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
        target_names=["Fail", "Pass"],
        zero_division=0
    )
)

# New student
new_student = np.array([
    [6, 85, 72]
])

prediction = model.predict(new_student)[0]

probability = model.predict_proba(new_student)[0]

result = "PASS 🎉" if prediction == 1 else "FAIL 📚"

print("\n🔮 NEW STUDENT PREDICTION")
print("-" * 35)

print("Study Hours:", new_student[0][0])
print("Attendance:", new_student[0][1], "%")
print("Previous Marks:", new_student[0][2])

print("Fail Probability:",
      round(probability[0] * 100, 2), "%")

print("Pass Probability:",
      round(probability[1] * 100, 2), "%")

print("Final Prediction:", result)

print("\n" + "=" * 55)
print("✅ DAY 16 COMPLETED!")
print("🌳 Decision Tree model built successfully!")
