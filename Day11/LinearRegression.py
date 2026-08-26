---

## 💻 Code 1 — `linear_regression.py`

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

print("📈 LINEAR REGRESSION")
print("=" * 45)

# Training data
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
y = np.array([35, 43, 50, 58, 66, 73])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predictions
predictions = model.predict(X)

print("\n🧠 MODEL INFORMATION")
print("-" * 30)

print("Slope:", round(model.coef_[0], 2))
print("Intercept:", round(model.intercept_, 2))

print("\n🎯 PREDICTIONS")

for hours, actual, predicted in zip(
    X.flatten(), y, predictions
):
    print(
        f"{hours} hours → "
        f"Actual: {actual} | "
        f"Predicted: {predicted:.2f}"
    )

# Evaluation
mse = mean_squared_error(y, predictions)
r2 = r2_score(y, predictions)

print("\n📊 MODEL EVALUATION")
print("-" * 30)

print("Mean Squared Error:", round(mse, 2))
print("R² Score:", round(r2, 4))

# Predict new value
new_hours = np.array([[7]])
new_prediction = model.predict(new_hours)

print("\n🔮 NEW PREDICTION")
print("Study Hours:", new_hours[0][0])
print("Predicted Marks:", round(new_prediction[0], 2))

# Visualization
plt.figure(figsize=(8, 5))

plt.scatter(X, y, label="Actual Data")
plt.plot(X, predictions, label="Regression Line")

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)

plt.show()

print("\n✅ DAY 11 COMPLETED!")
