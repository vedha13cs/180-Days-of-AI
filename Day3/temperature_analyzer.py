import numpy as np

print("╔════════════════════════════════════╗")
print("║      🌡️ TEMPERATURE ANALYZER       ║")
print("╚════════════════════════════════════╝")

Temperature recorded for 7 days

temperatures = np.array([28, 31, 29, 35, 33, 30, 27])

print("\n📅 Weekly Temperatures:")
print(temperatures)

Calculations

average = np.mean(temperatures)
highest = np.max(temperatures)
lowest = np.min(temperatures)

Temperature difference

difference = highest - lowest

print("\n📊 WEEKLY ANALYSIS")
print("-" * 30)

print("🌡️ Average Temperature:", round(average, 2), "°C")
print("🔥 Highest Temperature:", highest, "°C")
print("❄️ Lowest Temperature:", lowest, "°C")
print("📏 Temperature Difference:", difference, "°C")

Temperatures above average

above_average = temperatures[temperatures > average]

print("\n📈 Temperatures Above Average:")
print(above_average)

Hot days

hot_days = temperatures[temperatures >= 33]

print("\n🔥 Hot Days (33°C or above):")
print(hot_days)

Cool days

cool_days = temperatures[temperatures < 30]

print("\n❄️ Cool Days (Below 30°C):")
print(cool_days)

print("\n" + "=" * 35)
print("✅ DAY 03 COMPLETED!")
print("📊 Data analyzed successfully!")
print("🚀 Ready for Day 04!")
