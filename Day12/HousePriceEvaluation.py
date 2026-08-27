import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

print("🏠 HOUSE PRICE MODEL EVALUATION")
print("=" * 50)

# House size in square feet
X = np.array([
    [600],
    [800],
    [1000],
    [1200],
    [1400],
    [1600],
    [1800],
    [2000],
    [2200],
    [2400],
    [2600],
    [2800]
])

# Price in lakhs
y = np.array([
    25,
    32,
    39,
    45,
    52,
    59,
    66,
    73,
    80,
    87,
    94,
    101
])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

print("\n📊 DATA SPLIT")
print("-" * 30)

print("Total samples:", len(X))
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

# Create model
model = LinearRegression()

# Train
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

print("\n🎯 TEST RESULTS")
print("-" * 35)

for size, actual, predicted in zip(
    X_test.flatten(),
    y_test,
    predictions
):
    print(
        f"{size} sq.ft → "
        f"Actual: ₹{actual}L | "
        f"Predicted: ₹{predicted:.2f}L"
    )

# Evaluation metrics
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\n📈 MODEL PERFORMANCE")
print("-" * 35)

print("MAE:", round(mae, 2))
print("MSE:", round(mse, 2))
print("R² Score:", round(r2, 4))

print("\n💡 Interpretation:")
print("Lower MAE and MSE generally indicate smaller prediction errors.")
print("R² closer to 1 generally indicates a stronger fit.")

print("\n" + "=" * 50)
print("✅ DAY 12 COMPLETED!")
print("🏠 House price model evaluated successfully!")
