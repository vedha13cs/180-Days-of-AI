import random

print("🎲 PROBABILITY BASICS")
print("=" * 40)

# Coin Toss
total_tosses = 1000
heads = 0
tails = 0

for _ in range(total_tosses):
    result = random.choice(["Heads", "Tails"])

    if result == "Heads":
        heads += 1
    else:
        tails += 1

print("\n🪙 COIN TOSS SIMULATION")
print("Total Tosses:", total_tosses)
print("Heads:", heads)
print("Tails:", tails)

print("Experimental Probability of Heads:",
      round(heads / total_tosses, 3))

# Dice Roll
total_rolls = 1000
six_count = 0

for _ in range(total_rolls):
    roll = random.randint(1, 6)

    if roll == 6:
        six_count += 1

print("\n🎲 DICE SIMULATION")
print("Total Rolls:", total_rolls)
print("Number of 6s:", six_count)

print("Experimental Probability of 6:",
      round(six_count / total_rolls, 3))

print("\n📌 Theoretical Probability of 6: 1/6")
print("≈ 0.167")

print("\n" + "=" * 40)
print("✅ DAY 08 COMPLETED!")
print("🎲 Probability practice completed.")
