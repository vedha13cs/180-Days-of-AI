import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

print("🏠 HOUSE PRICE PREDICTOR")
print("=" * 50)

# Features:
# [Size in sq.ft, Bedrooms, Bathrooms]
X = np.array([
    [700, 1, 1],
    [900, 2, 1],
    [1100, 2, 2],
    [1300, 3, 2],
    [1500, 3, 2],
    [1700, 3, 3],
    [1900, 4, 3],
    [2100, 4, 3],
    [2300, 4, 4],
    [2500, 5, 4],
    [2700, 5, 4],
    [3000, 5, 5]
])

# Target: Price in lakhs
y = np.array([
    28, 35, 43, 50,
    58, 66, 74, 82,
    90, 98, 107, 120
])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

print("\n🧠 MODEL TRAINED")

print("\n📌 FEATURE COEFFICIENTS")
print("-" * 35)

print("Size:", round(model.coef_[0], 3))
print("Bedrooms:", round(model.coef_[1], 3))
print("Bathrooms:", round(model.coef_[2], 3))

print("\nIntercept:", round(model.intercept_, 3))

# Predict test data
predictions = model.predict(X_test)

print("\n🎯 TEST RESULTS")
print("-" * 40)

for features, actual, predicted in zip(
    X_test,
    y_test,
    predictions
):
    print(
        f"{features[0]} sq.ft, "
        f"{features[1]} bedrooms, "
        f"{features[2]} bathrooms → "
        f"Actual: ₹{actual}L | "
        f"Predicted: ₹{predicted:.2f}L"
    )

# Evaluation
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\n📊 MODEL PERFORMANCE")
print("-" * 35)

print("MAE:", round(mae, 2))
print("R² Score:", round(r2, 4))

# New house prediction
new_house = np.array([[1800, 3, 2]])

price = model.predict(new_house)

print("\n🔮 NEW HOUSE PREDICTION")
print("-" * 35)

print("Size:", new_house[0][0], "sq.ft")
print("Bedrooms:", new_house[0][1])
print("Bathrooms:", new_house[0][2])
print("Estimated Price: ₹", round(price[0], 2), "Lakhs")

print("\n" + "=" * 50)
print("✅ DAY 13 COMPLETED!")
print("🏠 Multi-feature prediction successful!")
