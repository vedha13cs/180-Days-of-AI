import pandas as pd
import matplotlib.pyplot as plt

print("🎓 STUDENT PERFORMANCE — EDA")
print("=" * 45)

data = {
    "Name": ["Asha", "Rahul", "Vedha", "Sneha", "Kiran",
             "Anu", "Ravi", "Meena"],
    "Python": [85, 72, 94, 68, 88, 91, 76, 83],
    "Math": [90, 65, 87, 74, 92, 89, 81, 86],
    "AI": [88, 70, 96, 72, 85, 94, 79, 90]
}

df = pd.DataFrame(data)

# Average marks
df["Average"] = df[["Python", "Math", "AI"]].mean(axis=1)

print("\n📋 STUDENT DATA")
print(df)

# Basic statistics
print("\n📊 SUBJECT AVERAGES")
print("-" * 30)

print("Python:", round(df["Python"].mean(), 2))
print("Math:", round(df["Math"].mean(), 2))
print("AI:", round(df["AI"].mean(), 2))

# Top student
top_student = df.loc[df["Average"].idxmax()]

print("\n🏆 TOP PERFORMER")
print("Name:", top_student["Name"])
print("Average:", round(top_student["Average"], 2))

# Pass percentage
passed = df[df["Average"] >= 40]
pass_percentage = (len(passed) / len(df)) * 100

print("\n✅ PASS PERCENTAGE")
print(round(pass_percentage, 2), "%")

# Correlation
print("\n🔗 CORRELATION")
print(df[["Python", "Math", "AI"]].corr())

# Visualization
plt.figure(figsize=(9, 5))

plt.bar(df["Name"], df["Average"])

plt.title("🎓 Student Average Performance")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.grid(axis="y")

plt.show()

print("\n" + "=" * 45)
print("✅ DAY 09 COMPLETED!")
print("🔎 EDA successfully performed!")
print("🚀 Ready for Day 10!")
