import pandas as pd

print("🎓 STUDENT DATA ANALYZER")
print("=" * 40)

data = {
    "Name": ["Asha", "Rahul", "Vedha", "Sneha", "Kiran", "Anu"],
    "Python": [85, 72, 91, 68, 88, 95],
    "Math": [90, 65, 87, 74, 92, 89],
    "AI": [88, 70, 94, 72, 85, 96]
}

df = pd.DataFrame(data)

# Calculate average
df["Average"] = df[["Python", "Math", "AI"]].mean(axis=1)

print("\n📋 STUDENT DATA")
print(df)

# Overall average
overall_average = df["Average"].mean()

print("\n📊 Overall Class Average:")
print(round(overall_average, 2))

# Highest scorer
top_student = df.loc[df["Average"].idxmax()]

print("\n🏆 TOP PERFORMER")
print("Name:", top_student["Name"])
print("Average:", round(top_student["Average"], 2))

# Students above class average
above_average = df[df["Average"] > overall_average]

print("\n🌟 Students Above Class Average:")
print(above_average[["Name", "Average"]])

# Students with AI marks above 90
ai_top = df[df["AI"] > 90]

print("\n🤖 Students With AI Marks Above 90:")
print(ai_top[["Name", "AI"]])

print("\n" + "=" * 40)
print("✅ DAY 04 COMPLETED!")
print("🐼 Data analyzed using Pandas.")
print("🚀 Keep learning. Keep building.")
