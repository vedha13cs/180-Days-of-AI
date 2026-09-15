import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import (
    apriori,
    association_rules
)

# Shopping transactions
transactions = [
    ["Milk", "Bread", "Butter"],
    ["Bread", "Butter"],
    ["Milk", "Bread"],
    ["Milk", "Butter"],
    ["Bread", "Butter", "Eggs"],
    ["Milk", "Bread", "Eggs"],
    ["Milk", "Bread", "Butter"],
    ["Bread", "Eggs"]
]

# Convert transactions into a one-hot encoded table
encoder = TransactionEncoder()

encoded_data = encoder.fit(
    transactions
).transform(transactions)

df = pd.DataFrame(
    encoded_data,
    columns=encoder.columns_
)

print("Transaction Data:")
print(df)

# Find frequent itemsets
frequent_items = apriori(
    df,
    min_support=0.25,
    use_colnames=True
)

print("\nFrequent Itemsets:")
print(frequent_items)

# Generate association rules
rules = association_rules(
    frequent_items,
    metric="confidence",
    min_threshold=0.50
)

# Select useful columns
rules = rules[
    [
        "antecedents",
        "consequents",
        "support",
        "confidence",
        "lift"
    ]
]

print("\nAssociation Rules:")
print(rules.sort_values(
    by="lift",
    ascending=False
))
