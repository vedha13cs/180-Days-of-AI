import numpy as np
from statistics import mode

print("📐 STATISTICS BASICS")
print("=" * 40)

data = np.array([10, 20, 20, 30, 40, 20, 50])

print("\n📊 Dataset:")
print(data)

mean = np.mean(data)
median = np.median(data)
data_mode = mode(data)
data_range = np.max(data) - np.min(data)
variance = np.var(data)
standard_deviation = np.std(data)

print("\n📈 STATISTICAL ANALYSIS")
print("-" * 35)

print("Mean:", mean)
print("Median:", median)
print("Mode:", data_mode)
print("Range:", data_range)
print("Variance:", round(variance, 2))
print("Standard Deviation:", round(standard_deviation, 2))

print("\n" + "=" * 40)
print("✅ DAY 07 COMPLETED!")
print("📐 Statistics foundation started!")
