🛒 DAY 27/180 — ASSOCIATION RULE LEARNING

«“AI can discover what people choose together — and turn those patterns into useful insights.” 🧠»

---

🌱 Today's Learning

Today I learned about Association Rule Learning.

It is an Unsupervised Learning technique used to discover interesting relationships and patterns between items in a dataset.

A common application is:

🛍️ Market Basket Analysis

---

🧠 What is Association Rule Learning?

Association Rule Learning finds relationships between items.

For example, if many customers purchase:

🍞 Bread + 🥛 Milk

the algorithm may discover that these products are frequently purchased together.

A rule can look like:

Bread → Milk

Meaning:

«Customers who purchase bread may also be likely to purchase milk.»

---

🛒 Market Basket Analysis

Market Basket Analysis analyzes customer transactions to discover purchasing patterns.

Example:

Transaction 1 → Bread, Milk, Butter
Transaction 2 → Bread, Milk
Transaction 3 → Bread, Butter
Transaction 4 → Milk, Butter

The algorithm looks for combinations that occur frequently.

---

🔑 Important Terms

1️⃣ Support

Support tells us how frequently an itemset appears in the entire dataset.

Formula:

Support(A) =
Transactions containing A
─────────────────────────
Total Transactions

Example:

If Bread appears in 3 out of 5 transactions:

Support(Bread) = 3/5 = 0.60

---

2️⃣ Confidence

Confidence tells us how often B appears when A appears.

For:

A → B

Formula:

Confidence(A → B)
=
Support(A and B)
────────────────
Support(A)

Higher confidence means the rule occurs more consistently.

---

3️⃣ Lift

Lift measures how much more often A and B occur together compared with what would be expected if they were independent.

Formula:

Lift(A → B)
=
Confidence(A → B)
────────────────
Support(B)

Interpretation

Lift > 1 → Positive association
Lift = 1 → Little/no association
Lift < 1 → Negative association

---

🔄 Association Rule Structure

A rule generally looks like:

Antecedent → Consequent

Example:

🍞 Bread → 🥛 Milk

Antecedent

The item on the left.

Bread

Consequent

The item on the right.

Milk

---

⚙️ Apriori Algorithm

One popular algorithm for association rule mining is:

🔹 Apriori

Apriori finds frequently occurring item combinations and generates association rules from them.

Basic workflow:

Transactions
     ↓
Find Frequent Itemsets
     ↓
Generate Rules
     ↓
Calculate Support
     ↓
Calculate Confidence
     ↓
Calculate Lift
     ↓
Select Useful Rules

---

💻 Today's Practice

🔹 01 — Association Basics

File:

association_basics.py

Practiced:

- Creating transactions
- Counting item combinations
- Understanding support
- Understanding confidence
- Understanding lift

---

🔹 02 — Market Basket Analysis

File:

market_basket_analysis.py

Created a small shopping dataset and used Apriori to discover useful product relationships.

---

🌍 Real-World Applications

Association Rule Learning is used in:

🛒 Online shopping
🛍️ Supermarkets
🎯 Marketing
📢 Product recommendations
💳 Customer behavior analysis
📊 Sales analysis
🎬 Recommendation systems

---

🧠 KEY TAKEAWAYS

✔ Association Rule Learning discovers relationships between items

✔ Market Basket Analysis is a common application

✔ Support measures frequency

✔ Confidence measures rule reliability

✔ Lift measures the strength of association

✔ Apriori is a popular association rule algorithm

✔ Rules follow the form A → B

---

📊 MY 180-DAY AI JOURNEY

🔥 Progress: 27 / 180

██████░░░░░░░░░░░░░░ 15.00%

✅ Completed

Day 01 → AI Fundamentals
Day 02 → NumPy
Day 03 → NumPy Operations
Day 04 → Pandas
Day 05 → Data Cleaning
Day 06 → Data Visualization
Day 07 → Statistics
Day 08 → Probability
Day 09 → EDA
Day 10 → Machine Learning Introduction
Day 11 → Linear Regression
Day 12 → Train/Test Split
Day 13 → Multiple Linear Regression
Day 14 → Logistic Regression
Day 15 → Model Evaluation
Day 16 → Decision Trees
Day 17 → Random Forest
Day 18 → KNN
Day 19 → SVM
Day 20 → Naive Bayes
Day 21 → Model Comparison
Day 22 → Cross-Validation & Hyperparameter Tuning
Day 23 → K-Means Clustering
Day 24 → Hierarchical Clustering
Day 25 → DBSCAN Clustering
Day 26 → PCA & Dimensionality Reduction
⭐ Day 27 → Association Rule Learning

🔜 NEXT

Day 28 → Recommendation Systems 🎯

---

💭 Today's Reflection

Today I learned that AI can discover relationships hidden inside everyday transactions.

A simple shopping basket can contain valuable patterns that help businesses understand what customers are likely to buy together.

27 days completed.
153 days to go. 🚀

---

«“Consistency over motivation.”»

#AI #MachineLearning #AssociationRules #Apriori #MarketBasketAnalysis #Python #DataScience #LearningInPublic #180DaysOfAI #GitHub
