import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import accuracy_score

print("🎓 STUDENT CLASSIFIER COMPARISON")
print("=" * 55)

# Student dataset
# [Study Hours, Attendance %, Previous Marks]

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

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Scaling
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    "Logistic Regression": LogisticRegression(
        max_iter=1000
    ),

    "Decision Tree": DecisionTreeClassifier(
        max_depth=4,
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42
    ),

    "KNN": KNeighborsClassifier(
        n_neighbors=5
    ),

    "SVM": SVC(
        kernel="rbf"
    ),

    "Naive Bayes": GaussianNB()
}

print("\n📊 ACCURACY COMPARISON")
print("-" * 40)

scores = {}

for name, model in models.items():

    model.fit(
        X_train_scaled,
        y_train
    )

    predictions = model.predict(
        X_test_scaled
    )

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    scores[name] = accuracy

    print(
        f"{name:<22} "
        f"{accuracy * 100:.2f}%"
    )

# Find best model
best_model = max(
    scores,
    key=scores.get
)

print("\n🏆 BEST MODEL")
print("-" * 40)

print("Model:", best_model)
print(
    "Accuracy:",
    round(scores[best_model] * 100, 2),
    "%"
)

# Prediction using best model
final_model = models[best_model]

new_student = np.array([
    [6.5, 85, 72]
])

new_student_scaled = scaler.transform(
    new_student
)

final_model.fit(
    X_train_scaled,
    y_train
)

prediction = final_model.predict(
    new_student_scaled
)[0]

result = "PASS 🎉" if prediction == 1 else "FAIL 📚"

print("\n🔮 NEW STUDENT")
print("-" * 40)

print("Study Hours:", new_student[0][0])
print("Attendance:", new_student[0][1], "%")
print("Previous Marks:", new_student[0][2])
print("Prediction:", result)

print("\n" + "=" * 55)
print("✅ DAY 21 COMPLETED!")
print("🎓 Model comparison completed successfully!")
