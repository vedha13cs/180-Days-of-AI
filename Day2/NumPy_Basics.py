# 🤖 180 Days of AI
# Day 02 - NumPy Basics

import numpy as np

print("🚀 Day 02 - NumPy Basics")
print("=" * 35)

# Creating a 1D array
numbers = np.array([10, 20, 30, 40, 50])

print("\n📌 1D Array:")
print(numbers)

print("\n📊 Array Information:")
print("Dimensions:", numbers.ndim)
print("Shape:", numbers.shape)
print("Size:", numbers.size)

# Creating a 2D array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n🧮 2D Array:")
print(matrix)

print("\n📊 2D Array Information:")
print("Dimensions:", matrix.ndim)
print("Shape:", matrix.shape)
print("Size:", matrix.size)

# Indexing
print("\n🔍 Indexing:")
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Basic calculations
print("\n📈 Calculations:")
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))

# Special arrays
print("\n✨ Special Arrays:")
print("Zeros:", np.zeros(5))
print("Ones:", np.ones(5))
print("Range:", np.arange(1, 11))

print("\n✅ Day 02 Completed!")
print("Keep learning. Keep building. 🔥")
