import pandas as pd
import matplotlib.pyplot as plt

print("📊 BASIC EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 45)

# Create sample dataset
data = {
    "Name": ["Asha", "Rahul", "Vedha", "Sneha", "Kiran",
             "Anu", "Ravi", "Meena"],
    "Age": [20, 21, 20, 22, 21, 20, 22, 21],
    "Marks": [85, 72, 94, 68, 88, 91, 76, 83],
    "Attendance": [90, 82, 95, 75, 88, 92, 80, 86]
}

df = pd.DataFrame(data)

# Display data
print("\n📋 DATASET")
print(df)

# First 5 rows
print("\n🔍 FIRST 5 ROWS")
print(df.head())

# Dataset information
print("\nℹ️ DATASET INFORMATION")
print(df.info())

# Basic statistics
print("\n📊 BASIC STATISTICS")
print(df.describe())

# Check missing values
print("\n❓ MISSING VALUES")
print(df.isnull().sum())

# Average marks
print("\n🎯 AVERAGE MARKS")
print("Average Marks:", round(df["Marks"].mean(), 2))

# Highest marks
print("\n🏆 HIGHEST MARKS")
top_student = df.loc[df["Marks"].idxmax()]
print("Name:", top_student["Name"])
print("Marks:", top_student["Marks"])

# Lowest marks
print("\n📉 LOWEST MARKS")
low_student = df.loc[df["Marks"].idxmin()]
print("Name:", low_student["Name"])
print("Marks:", low_student["Marks"])

# Correlation
print("\n🔗 CORRELATION")
print(df[["Age", "Marks", "Attendance"]].corr())

# Visualization
plt.figure(figsize=(9, 5))

plt.bar(df["Name"], df["Marks"])

plt.title("📊 Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.grid(axis="y")

plt.show()

print("\n" + "=" * 45)
print("✅ EDA BASICS COMPLETED!")
print("🔎 Data successfully explored!")
print("🚀 Ready for the next step!")
