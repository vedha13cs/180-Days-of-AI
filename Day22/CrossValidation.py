import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    StratifiedKFold
)

from sklearn.metrics import accuracy_score


print("🧪 CROSS-VALIDATION WITH RANDOM FOREST")
print("=" * 60)


# Features:
# [Study Hours, Attendance, Previous Marks]

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
    [8.5, 91, 82],
    [4.2, 73, 56],
    [7.2, 86, 76],
    [5.8, 79, 67],
    [9.5, 94, 89],
    [3.8, 71, 54],
    [6.8, 83, 71],
    [5.2, 77, 63],
    [8.8, 93, 86]
])


# 0 = Fail
# 1 = Pass

y = np.array([
    0, 0, 0, 0,
    1, 1, 1, 1,
    1, 1, 1, 1,
    0, 0, 1, 1,
    1, 1, 1, 1,
    0, 1, 1, 1
])


# Keep a final test set separate
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)


# Create model
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42
)


# 5-Fold Stratified Cross-Validation
cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)


scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=cv,
    scoring="accuracy"
)


print("\n📊 CROSS-VALIDATION SCORES")
print("-" * 40)

for i, score in enumerate(scores, start=1):
    print(
        f"Fold {i}: "
        f"{score * 100:.2f}%"
    )


print("\n📈 AVERAGE CV SCORE")
print("-" * 40)

print(
    "Average:",
    round(scores.mean() * 100, 2),
    "%"
)


print(
    "Standard Deviation:",
    round(scores.std() * 100, 2),
    "%"
)


# Train final model on training data
model.fit(X_train, y_train)


# Evaluate on untouched test set
predictions = model.predict(X_test)

test_accuracy = accuracy_score(
    y_test,
    predictions
)


print("\n🎯 FINAL TEST PERFORMANCE")
print("-" * 40)

print(
    "Test Accuracy:",
    round(test_accuracy * 100, 2),
    "%"
)


print("\n" + "=" * 60)
print("✅ DAY 22 CROSS-VALIDATION COMPLETED!")
