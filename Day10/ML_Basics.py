# 🤖 Day 10 - Machine Learning Basics

import numpy as np
from sklearn.linear_model import LinearRegression

print("🤖 FIRST MACHINE LEARNING MODEL")
print("=" * 45)

# Training data
# Study hours → Marks
study_hours = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
marks = np.array([35, 42, 50, 58, 67, 75])

print("\n📊 Training Data")
print("-" * 30)

for hours, mark in zip(study_hours.flatten(), marks):
    print(f"Study Hours: {hours} → Marks: {mark}")

# Create model
model = LinearRegression()

# Train model
model.fit(study_hours, marks)

print("\n🧠 MODEL TRAINED!")

print("Slope:", round(model.coef_[0], 2))
print("Intercept:", round(model.intercept_, 2))

# Make prediction
new_hours = np.array([[7]])

prediction = model.predict(new_hours)

print("\n🎯 PREDICTION")
print("-" * 30)
print("Study Hours:", new_hours[0][0])
print("Predicted Marks:", round(prediction[0], 2))

print("\n" + "=" * 45)
print("✅ DAY 10 COMPLETED!")
print("🚀 My first ML model is working!")
