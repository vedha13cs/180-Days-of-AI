import matplotlib.pyplot as plt

print("📊 MATPLOTLIB VISUALIZATION BASICS")
print("=" * 40)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
study_hours = [2, 3, 2.5, 4, 3.5, 5, 4]

# Line chart
plt.figure(figsize=(8, 5))
plt.plot(days, study_hours, marker="o")
plt.title("My Weekly AI Study Hours")
plt.xlabel("Day")
plt.ylabel("Study Hours")
plt.grid(True)
plt.show()

# Bar chart
plt.figure(figsize=(8, 5))
plt.bar(days, study_hours)
plt.title("Weekly Study Hours")
plt.xlabel("Day")
plt.ylabel("Hours")
plt.show()

print("\n✅ Day 6 visualization practice completed!")
