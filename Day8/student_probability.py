import numpy as np

print("🎓 STUDENT PERFORMANCE PROBABILITY")
print("=" * 45)

marks = np.array([45, 67, 82, 91, 56, 74, 88, 39, 95, 61])

print("\n📊 Student Marks:")
print(marks)

total_students = len(marks)

# Probability of scoring 60 or more
students_60_plus = np.sum(marks >= 60)
probability_60_plus = students_60_plus / total_students

# Probability of scoring 80 or more
students_80_plus = np.sum(marks >= 80)
probability_80_plus = students_80_plus / total_students

# Probability of failing
students_failed = np.sum(marks < 40)
probability_failed = students_failed / total_students

print("\n📈 PROBABILITY ANALYSIS")
print("-" * 35)

print(
    "P(Marks >= 60):",
    round(probability_60_plus, 2)
)

print(
    "P(Marks >= 80):",
    round(probability_80_plus, 2)
)

print(
    "P(Marks < 40):",
    round(probability_failed, 2)
)

print("\n📌 In Percentage:")

print(
    "60+ Marks:",
    round(probability_60_plus * 100, 2), "%"
)

print(
    "80+ Marks:",
    round(probability_80_plus * 100, 2), "%"
)

print(
    "Below 40:",
    round(probability_failed * 100, 2), "%"
)

print("\n" + "=" * 45)
print("✅ DAY 08 COMPLETED!")
print("🚀 Keep learning. Keep building.")
