import matplotlib.pyplot as plt

students = ["Asha", "Rahul", "Vedha", "Sneha", "Kiran"]
marks = [85, 72, 94, 68, 88]

# Bar chart
plt.figure(figsize=(8, 5))
plt.bar(students, marks)

plt.title("🎓 Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.grid(axis="y")

plt.show()

# Line chart
plt.figure(figsize=(8, 5))
plt.plot(students, marks, marker="o")

plt.title("📈 Student Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.grid(True)

plt.show()

# Find highest scorer
highest_index = marks.index(max(marks))

print("🏆 Top Performer:", students[highest_index])
print("📊 Highest Mark:", marks[highest_index])

print("\n✅ DAY 06 COMPLETED!")
