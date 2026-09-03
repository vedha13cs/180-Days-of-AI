import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score 

print("⚡ SUPPORT VECTOR MACHINE")
print("=" * 50)

# Features:
# [Study Hours, Previous Marks]

X = np.array([
    [1, 40],
    [2, 45],
    [2.5, 48],
    [3, 52],
    [3.5, 55],
    [4, 60],
    [5, 65],
    [5.5, 68],
    [6, 72],
    [7, 76],
    [8, 82],
    [9, 88],
    [10, 92]
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

# Scale features
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create SVM
model = SVC(
    kernel="linear",
    C=1.0,
    probability=True,
    random_state=42
)

# Train
model.fit(X_train_scaled, y_train)

print("\n⚡ SVM MODEL TRAINED")
print("Kernel:", model.kernel)
print("C:", model.C)

# Predictions
predictions = model.predict(X_test_scaled)

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

# New student
new_student = np.array([
    [6.5, 70]
])

new_student_scaled = scaler.transform(new_student)

prediction = model.predict(new_student_scaled)[0]
probability = model.predict_proba(new_student_scaled)[0]

result = "PASS 🎉" if prediction == 1 else "FAIL 📚"

print("\n🔮 NEW PREDICTION")
print("-" * 35)

print("Study Hours:", new_student[0][0])
print("Previous Marks:", new_student[0][1])

print(
    "Pass Probability:",
    round(probability[1] * 100, 2),
    "%"
)

print("Prediction:", result)

print("\n" + "=" * 50)
print("✅ DAY 19 COMPLETED!")
