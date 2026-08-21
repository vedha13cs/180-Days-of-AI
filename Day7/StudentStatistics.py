import numpy as np
import matplotlib.pyplot as plt

students = ["Asha", "Rahul", "Vedha", "Sneha", "Kiran", "Anu"]
marks = np.array([78, 85, 92, 67, 88, 95])

print("🎓 STUDENT STATISTICS ANALYZER")
print("=" * 40)

mean = np.mean(marks)
median = np.median(marks)
highest = np.max(marks)
lowest = np.min(marks)
std = np.std(marks)

print("\n📊 Student Marks:")
for student, mark in zip(students, marks):
    print(student, ":", mark)

print("\n📈 STATISTICS")
print("-" * 30)

print("Mean:", round(mean, 2))
print("Median:", median)
print("Highest:", highest)
print("Lowest:", lowest)
print("Standard Deviation:", round(std, 2))

# Students above average
above_average = marks[marks > mean]

print("\n🌟 Marks Above Average:")
print(above_average)

# Visualization
plt.figure(figsize=(8, 5))
plt.bar(students, marks)

plt.axhline(
    mean,
    linestyle="--",
    label=f"Average = {mean:.2f}"
)

plt.title("🎓 Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.legend()
plt.grid(axis="y")

plt.show()

print("\n✅ DAY 07 COMPLETED!")
print("🚀 Keep learning. Keep building.")
