import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

print("🏠 HOUSE PRICE PREDICTOR")
print("=" * 45)

# House size in square feet
X = np.array([
    [800],
    [1000],
    [1200],
    [1500],
    [1800],
    [2000]
])

# House prices in lakhs
y = np.array([
    30,
    38,
    45,
    55,
    65,
    72
])

# Create model
model = LinearRegression()

# Train
model.fit(X, y)

print("\n🧠 MODEL TRAINED")
print("-" * 30)

print("Slope:", round(model.coef_[0], 4))
print("Intercept:", round(model.intercept_, 2))

# Training predictions
predictions = model.predict(X)

print("\n📊 TRAINING DATA")

for size, actual, predicted in zip(
    X.flatten(), y, predictions
):
    print(
        f"{size} sq.ft → "
        f"Actual: ₹{actual}L | "
        f"Predicted: ₹{predicted:.2f}L"
    )

# Model score
score = r2_score(y, predictions)

print("\n📈 R² SCORE:", round(score, 4))

# New prediction
size = float(
    input("\n🏠 Enter house size in sq.ft: ")
)

prediction = model.predict([[size]])

print("\n🔮 PREDICTED PRICE")
print("-" * 30)
print(f"House Size: {size} sq.ft")
print(f"Estimated Price: ₹{prediction[0]:.2f} Lakhs")

print("\n" + "=" * 45)
print("✅ DAY 11 COMPLETED!")
print("🏠 Prediction generated successfully!")
