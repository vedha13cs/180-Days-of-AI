import numpy as np

print("╔════════════════════════════════════╗")
print("║     🧮 NUMPY ARRAY OPERATIONS      ║")
print("╚════════════════════════════════════╝")

Creating an array

numbers = np.array([10, 20, 30, 40, 50])

print("\n📌 Original Array:")
print(numbers)

Indexing

print("\n🔍 INDEXING")
print("First element:", numbers[0])
print("Third element:", numbers[2])
print("Last element:", numbers[-1])

Slicing

print("\n✂️ SLICING")
print("First three elements:", numbers[:3])
print("Elements from index 2:", numbers[2:])
print("Middle elements:", numbers[1:4])

Mathematical operations

print("\n🧮 ARRAY OPERATIONS")

print("Addition:", numbers + 5)
print("Subtraction:", numbers - 5)
print("Multiplication:", numbers * 2)
print("Division:", numbers / 2)

Filtering

print("\n🔎 FILTERING")

greater_than_25 = numbers[numbers > 25]
print("Numbers greater than 25:", greater_than_25)

even_numbers = numbers[numbers % 2 == 0]
print("Even numbers:", even_numbers)

Reshaping

matrix = np.arange(1, 10).reshape(3, 3)

print("\n🔄 RESHAPING")
print("3 × 3 Matrix:")
print(matrix)

print("\n📊 Matrix Shape:", matrix.shape)
print("📦 Matrix Size:", matrix.size)

print("\n" + "=" * 35)
print("✅ DAY 03 COMPLETED!")
print("🚀 Keep learning. Keep building.")
