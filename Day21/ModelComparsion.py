import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

print("🔬 MACHINE LEARNING MODEL COMPARISON")
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

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Scaling for models that depend on feature scale
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(
        max_depth=4,
        random_state=42
    ),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42
    ),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "SVM": SVC(kernel="rbf"),
    "Naive Bayes": GaussianNB()
}

print("\n📊 MODEL RESULTS")
print("-" * 60)

results = []

for name, model in models.items():

    # Tree and Naive Bayes can work without scaling.
    # For a fair comparison, scaling is also acceptable,
    # but here we use scaled data consistently.

    model.fit(X_train_scaled, y_train)

    predictions = model.predict(X_test_scaled)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(
        y_test,
        predictions,
        zero_division=0
    )
    recall = recall_score(
        y_test,
        predictions,
        zero_division=0
    )
    f1 = f1_score(
        y_test,
        predictions,
        zero_division=0
    )

    results.append(
        (name, accuracy, precision, recall, f1)
    )

    print(f"\n{name}")
    print(f"Accuracy : {accuracy:.3f}")
    print(f"Precision: {precision:.3f}")
    print(f"Recall   : {recall:.3f}")
    print(f"F1 Score : {f1:.3f}")

# Find model with highest F1
best_model = max(
    results,
    key=lambda result: result[4]
)

print("\n🏆 BEST MODEL BY F1 SCORE")
print("-" * 40)

print("Model:", best_model[0])
print("F1 Score:", round(best_model[4], 3))

print("\n" + "=" * 60)
print("✅ DAY 21 COMPLETED!")
print("🔬 Multiple models compared successfully!")
