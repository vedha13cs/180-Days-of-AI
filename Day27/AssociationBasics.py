from collections import Counter
from itertools import combinations

# Sample transactions
transactions = [
    ["Bread", "Milk", "Butter"],
    ["Bread", "Milk"],
    ["Bread", "Butter"],
    ["Milk", "Butter"],
    ["Bread", "Milk", "Butter"]
]

total_transactions = len(transactions)

# Count individual items
item_counts = Counter()

for transaction in transactions:
    for item in transaction:
        item_counts[item] += 1

print("Item Frequencies:")

for item, count in item_counts.items():
    support = count / total_transactions

    print(
        f"{item}: "
        f"Count = {count}, "
        f"Support = {support:.2f}"
    )


# Find pair frequencies
pair_counts = Counter()

for transaction in transactions:
    for pair in combinations(sorted(transaction), 2):
        pair_counts[pair] += 1

print("\nPair Frequencies:")

for pair, count in pair_counts.items():
    support = count / total_transactions

    print(
        f"{pair}: "
        f"Count = {count}, "
        f"Support = {support:.2f}"
    )
