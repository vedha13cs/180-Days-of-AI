import pandas as pd

print("🐼 PANDAS BASICS")
print("=" * 35)

# Creating a Series
marks = pd.Series([85, 92, 76, 88, 95])

print("\n📊 Series:")
print(marks)

# Creating a DataFrame
data = {
    "Name": ["Vedha", "Anu", "Rahul", "Sneha", "Kiran"],
    "Age": [21, 20, 21, 22, 20],
    "Marks": [85, 92, 76, 88, 95]
}

df = pd.DataFrame(data)

print("\n📋 DataFrame:")
print(df)

print("\n🔍 First 3 Records:")
print(df.head(3))

print("\n📐 Shape:")
print(df.shape)

print("\n📌 Columns:")
print(df.columns.tolist())

print("\n📈 Statistics:")
print(df.describe())

print("\n🏆 Average Marks:")
print(df["Marks"].mean())

print("\n✅ Day 4 completed!")
