# 🎯 Day 10 - First ML Prediction


import numpy as np
from sklearn.linear_model import LinearRegression

print("📚 STUDY HOURS → MARKS PREDICTOR")
print("=" * 45)

# Example training dataset
X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7]
])

y = np.array([
    35,
    43,
    50,
    58,
    66,
    73,
    80
])

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Get user input
hours = float(input("\n⏱️ Enter your study hours: "))

# Prediction
prediction = model.predict([[hours]])

print("\n📊 RESULT")
print("-" * 30)
print("Study Hours:", hours)
print("Predicted Marks:", round(prediction[0], 2))

if prediction[0] >= 75:
    print("🏆 Great predicted performance!")
elif prediction[0] >= 50:
    print("👍 Good predicted performance!")
else:
    print("📚 Keep practicing!")

print("\n" + "=" * 45)
print("✅ Prediction completed!")
print("🤖 Machine Learning in action!")
