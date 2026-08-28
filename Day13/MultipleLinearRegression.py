import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

print("📈 MULTIPLE LINEAR REGRESSION")
print("=" * 45)

# Features:
# [Study Hours, Practice Problems, Attendance]
X = np.array([
    [2, 10, 70],
    [3, 15, 75],
    [4, 20, 80],
    [5, 25, 85],
    [6, 30, 90],
    [7, 35, 92],
    [8, 40, 95],
    [9, 45, 97],
    [10, 50, 98],
    [11, 55, 99]
])

# Target: Exam Marks
y = np.array([
    45, 50, 56, 62, 68,
    74, 80, 85, 91, 95
])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = LinearRegression()

# Train
model.fit(X_train, y_train)

print("\n🧠 MODEL TRAINED")

print("\n📌 FEATURE COEFFICIENTS")
print("-" * 30)

print("Study Hours:", round(model.coef_[0], 3))
print("Practice Problems:", round(model.coef_[1], 3))
print("Attendance:", round(model.coef_[2], 3))

print("\nIntercept:", round(model.intercept_, 3))

# Predictions
predictions = model.predict(X_test)

print("\n🎯 TEST PREDICTIONS")
print("-" * 35)

for actual, predicted in zip(y_test, predictions):
    print(
        f"Actual: {actual} | "
        f"Predicted: {predicted:.2f}"
    )

# Evaluation
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\n📊 MODEL EVALUATION")
print("-" * 30)

print("MAE:", round(mae, 2))
print("R² Score:", round(r2, 4))

# New prediction
new_student = np.array([[6, 32, 90]])

new_prediction = model.predict(new_student)

print("\n🔮 NEW STUDENT PREDICTION")
print("-" * 30)

print("Study Hours:", new_student[0][0])
print("Practice Problems:", new_student[0][1])
print("Attendance:", new_student[0][2])
print("Predicted Marks:", round(new_prediction[0], 2))

print("\n" + "=" * 45)
print("✅ DAY 13 COMPLETED!")
