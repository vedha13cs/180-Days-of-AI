import pandas as pd

print("🧹 DATA CLEANING WITH PANDAS")
print("=" * 40)

# Dataset containing missing and duplicate values
data = {
    "Name": ["Asha", "Rahul", "Vedha", "Sneha", "Rahul", "Kiran"],
    "Age": [21, 20, None, 22, 20, 21],
    "Marks": [85, 76, 91, None, 76, 88]
}

df = pd.DataFrame(data)

print("\n📋 ORIGINAL DATA")
print(df)

# Check missing values
print("\n🔍 MISSING VALUES")
print(df.isnull().sum())

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\n🧹 AFTER FILLING MISSING VALUES")
print(df)

# Check duplicates
print("\n♻️ DUPLICATE RECORDS")
print(df.duplicated())

# Remove duplicates
df = df.drop_duplicates()

print("\n✨ CLEAN DATA")
print(df)

print("\n📊 Final Shape:", df.shape)

print("\n" + "=" * 40)
print("✅ DAY 05 COMPLETED!")
print("🧹 Data cleaned successfully!")
