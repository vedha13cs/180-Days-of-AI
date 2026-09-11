🌳 DAY 24/180 — HIERARCHICAL CLUSTERING

«“When data has no labels, patterns can still tell a story.” 🧠»

---

🌱 Today's Learning

Today I learned another important Unsupervised Learning technique:

🌳 Hierarchical Clustering

Hierarchical Clustering groups similar data points together and creates a tree-like structure of clusters.

This structure is called a:

🔹 Dendrogram

---

🧠 What is Hierarchical Clustering?

Hierarchical Clustering is an unsupervised machine learning technique used to discover groups in unlabeled data.

Instead of directly deciding the final groups, it builds a hierarchy of clusters.

Individual Data Points
        ↓
Small Groups
        ↓
Larger Groups
        ↓
One Large Group

---

🔄 Two Main Approaches

There are two types:

1️⃣ Agglomerative Clustering

This is the most commonly used approach.

It follows a bottom-up process.

Each point starts separately
          ↓
Similar points are combined
          ↓
Clusters continue merging
          ↓
One large cluster

2️⃣ Divisive Clustering

This follows a top-down approach.

One large cluster
       ↓
Split into smaller clusters
       ↓
Continue splitting

---

🌳 What is a Dendrogram?

A dendrogram is a tree-like diagram that shows how clusters are merged.

Example:

        ┌───────────────┐
        │               │
     ┌──┴──┐         ┌──┴──┐
     │     │         │     │
     A     B         C     D

It helps us understand the hierarchy of the data.

---

🔗 Linkage Methods

Hierarchical Clustering needs a method to decide which clusters should be joined.

Common linkage methods include:

🔹 Single Linkage

Uses the distance between the closest points.

🔹 Complete Linkage

Uses the distance between the farthest points.

🔹 Average Linkage

Uses the average distance between points.

🔹 Ward Linkage

Tries to minimize the variance within clusters.

---

⚙️ Basic Workflow

Collect Data
     ↓
Clean Data
     ↓
Scale Features
     ↓
Calculate Distances
     ↓
Build Hierarchy
     ↓
Create Dendrogram
     ↓
Choose Number of Clusters
     ↓
Create Final Clusters

---

📏 Why Feature Scaling?

Distance plays an important role in clustering.

If features have very different scales, one feature may dominate the distance calculation.

Therefore, we can use:

StandardScaler()

before clustering.

---

🔵 K-Means vs Hierarchical Clustering

K-Means| Hierarchical
Requires K beforehand| Can explore different cluster counts
Uses centroids| Builds hierarchy
Faster for large datasets| Can be more computationally expensive
No dendrogram| Uses dendrogram
Iterative centroid-based approach| Tree-based merging/splitting

---

💻 Today's Practice

🔹 01 — Hierarchical Basics

File:

hierarchical_basics.py

Practiced:

- Creating sample data
- Scaling data
- Applying Agglomerative Clustering
- Creating clusters
- Checking cluster labels

---

🔹 02 — Customer Clustering

File:

customer_hierarchical_clustering.py

Used customer information such as:

- Annual Income
- Spending Score

Goal:

«Find groups of customers with similar behavior.»

---

🌍 Real-World Applications

Hierarchical Clustering can be used for:

🧬 Biological data analysis
🛒 Customer segmentation
📚 Document grouping
🧪 Research analysis
🖼️ Image analysis
🧑‍🤝‍🧑 User grouping
📊 Exploratory data analysis

---

🧠 KEY TAKEAWAYS

✔ Hierarchical Clustering is Unsupervised Learning

✔ It groups similar data points

✔ Agglomerative follows a bottom-up approach

✔ Divisive follows a top-down approach

✔ Dendrogram represents the hierarchy

✔ Linkage determines how clusters are combined

✔ Feature scaling can be important

✔ AgglomerativeClustering is available in scikit-learn

---

📊 MY 180-DAY AI JOURNEY

🔥 Progress: 24 / 180

█████░░░░░░░░░░░░░░░ 13.33%

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
⭐ Day 24 → Hierarchical Clustering

🔜 NEXT

Day 25 → DBSCAN Clustering 🟣

---

💭 Today's Reflection

K-Means taught me how to create groups using centroids.

Today, Hierarchical Clustering showed me another way to understand relationships between data points — by building a hierarchy of clusters.

24 days completed.
156 days to go. 🚀

---

«“Consistency over motivation.”»

#AI #MachineLearning #Python #HierarchicalClustering #UnsupervisedLearning #DataScience #LearningInPublic #180DaysOfAI #GitHub
