import numpy as np

from sklearn.model_selection import (
    train_test_split,
    GridSearchCV
)

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report
)


print("⚙️ RANDOM FOREST HYPERPARAMETER TUNING")
print("=" * 65)


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


# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)


# Base model
model = RandomForestClassifier(
    random_state=42
)


# Hyperparameter combinations
param_grid = {

    "n_estimators": [
        50,
        100,
        150
    ],

    "max_depth": [
        3,
        5,
        7,
        None
    ],

    "min_samples_split": [
        2,
        4
    ]
}


print("\n🔎 SEARCHING HYPERPARAMETERS...")
print("-" * 45)


# Grid Search
grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)


# Train and search
grid_search.fit(
    X_train,
    y_train
)


print("\n🏆 BEST PARAMETERS")
print("-" * 45)

print(
    "Best Parameters:"
)

for parameter, value in grid_search.best_params_.items():

    print(
        f"{parameter}: {value}"
    )


print("\n📈 BEST CROSS-VALIDATION SCORE")
print("-" * 45)

print(
    round(
        grid_search.best_score_ * 100,
        2
    ),
    "%"
)


# Best model
best_model = grid_search.best_estimator_


# Test on unseen data
predictions = best_model.predict(
    X_test
)


test_accuracy = accuracy_score(
    y_test,
    predictions
)


print("\n🎯 TEST SET PERFORMANCE")
print("-" * 45)

print(
    "Test Accuracy:",
    round(test_accuracy * 100, 2),
    "%"
)


print("\n📋 CLASSIFICATION REPORT")
print("-" * 45)

print(
    classification_report(
        y_test,
        predictions,
        target_names=[
            "Fail",
            "Pass"
        ],
        zero_division=0
    )
)


# New student prediction
new_student = np.array([
    [6.5, 85, 72]
])


prediction = best_model.predict(
    new_student
)[0]


result = (
    "PASS 🎉"
    if prediction == 1
    else
    "FAIL 📚"
)


print("\n🔮 NEW STUDENT PREDICTION")
print("-" * 45)

print(
    "Study Hours:",
    new_student[0][0]
)

print(
    "Attendance:",
    new_student[0][1],
    "%"
)

print(
    "Previous Marks:",
    new_student[0][2]
)

print(
    "Prediction:",
    result
)


print("\n" + "=" * 65)
print("✅ DAY 22 COMPLETED!")
print("⚙️ Hyperparameters tuned successfully!")
