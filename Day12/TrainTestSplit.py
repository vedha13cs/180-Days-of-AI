---

# 💻 Code 1 — `train_test_split.py`

```python
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

print("🧪 TRAIN / TEST SPLIT")
print("=" * 45)

# Study hours
X = np.array([
    [1], [2], [3], [4], [5],
    [6], [7], [8], [9], [10]
])

# Marks
y = np.array([
    35, 42, 50, 57, 65,
    72, 78, 84, 89, 94
])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\n📊 DATASET")
print("Total samples:", len(X))

print("\n🧠 TRAINING DATA")
print("Training samples:", len(X_train))

print("\n🧪 TESTING DATA")
print("Testing samples:", len(X_test))

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict test data
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

print("\n📈 MODEL EVALUATION")
print("-" * 35)

print("Mean Absolute Error:", round(mae, 2))
print("R² Score:", round(r2, 4))

print("\n" + "=" * 45)
print("✅ DAY 12 COMPLETED!")
print("🧪 Model tested on unseen data.")
