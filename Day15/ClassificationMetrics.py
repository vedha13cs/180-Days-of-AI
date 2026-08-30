from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

print("📊 CLASSIFICATION MODEL EVALUATION")
print("=" * 50)

# 1 = Positive
# 0 = Negative

actual = [1, 1, 1, 1, 0, 0, 0, 0, 1, 0]

predicted = [1, 1, 0, 1, 0, 0, 1, 0, 1, 0]

# Calculate metrics
accuracy = accuracy_score(actual, predicted)
precision = precision_score(actual, predicted)
recall = recall_score(actual, predicted)
f1 = f1_score(actual, predicted)

# Confusion Matrix
matrix = confusion_matrix(actual, predicted)

print("\n📈 MODEL METRICS")
print("-" * 35)

print("Accuracy :", round(accuracy * 100, 2), "%")
print("Precision:", round(precision, 3))
print("Recall   :", round(recall, 3))
print("F1 Score :", round(f1, 3))

print("\n🔲 CONFUSION MATRIX")
print("-" * 35)

print(matrix)

print("\n📌 MATRIX FORMAT")
print("[[TN  FP]")
print(" [FN  TP]]")

print("\n" + "=" * 50)
print("✅ DAY 15 COMPLETED!")
print("📊 Classification metrics calculated.")
