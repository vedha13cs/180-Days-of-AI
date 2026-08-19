import pandas as pd

print("💰 SALES DATA ANALYZER")
print("=" * 40)

data = {
    "Product": [
        "Laptop",
        "Mouse",
        "Keyboard",
        "Laptop",
        "Headphones",
        "Mouse"
    ],
    "Quantity": [2, 10, 5, 1, 8, 7],
    "Price": [55000, 700, 1500, 55000, 2000, 700]
}

df = pd.DataFrame(data)

# Calculate total for each sale
df["Total"] = df["Quantity"] * df["Price"]

print("\n📋 SALES DATA")
print(df)

# Total revenue
total_revenue = df["Total"].sum()

# Average sale
average_sale = df["Total"].mean()

# Highest sale
highest_sale = df.loc[df["Total"].idxmax()]

print("\n📊 SALES SUMMARY")
print("-" * 35)

print("💰 Total Revenue:", total_revenue)
print("📈 Average Sale:", round(average_sale, 2))

print("\n🏆 HIGHEST SALE")
print("Product:", highest_sale["Product"])
print("Quantity:", highest_sale["Quantity"])
print("Total:", highest_sale["Total"])

# Sales above 5000
large_sales = df[df["Total"] > 5000]

print("\n🔥 SALES ABOVE ₹5,000")
print(large_sales)

print("\n" + "=" * 40)
print("✅ DAY 05 COMPLETED!")
print("🚀 Keep learning. Keep building.")
