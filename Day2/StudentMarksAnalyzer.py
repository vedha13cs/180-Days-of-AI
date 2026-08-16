import numpy as np

print("╔══════════════════════════════════╗")
print("║   🎓 STUDENT MARKS ANALYZER      ║")
print("╚══════════════════════════════════╝")

Marks of 5 students

marks = np.array([78, 85, 92, 67, 88])

print("\n📊 Student Marks:")
print(marks)

Basic analysis

total = np.sum(marks)
average = np.mean(marks)
highest = np.max(marks)
lowest = np.min(marks)

print("\n📈 RESULTS")
print("-" * 30)

print("👥 Number of Students:", marks.size)
print("🧮 Total Marks:", total)
print("📊 Average Marks:", round(average, 2))
print("🏆 Highest Mark:", highest)
print("📉 Lowest Mark:", lowest)

Find students scoring above average

above_average = marks[marks > average]

print("\n🌟 Marks Above Average:")
print(above_average)

Grade check

print("\n🎯 Performance:")

if average >= 90:
print("🏆 Excellent Performance!")
elif average >= 75:
print("🥇 Very Good Performance!")
elif average >= 60:
print("👍 Good Performance!")
else:
print("📚 Keep Practicing!")

print("\n" + "=" * 30)
print("✅ DAY 02 COMPLETED!")
print("🚀 Keep learning. Keep building.")
