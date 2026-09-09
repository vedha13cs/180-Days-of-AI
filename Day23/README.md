🚀 DAY 23/180 — K-MEANS CLUSTERING

«“Not every dataset gives us the answers. Sometimes, AI has to discover the groups itself.” 🤖»

---

🧠 What I Learned Today

Today I started Unsupervised Learning and learned one of its most popular algorithms:

🔹 K-Means Clustering

K-Means is a machine learning algorithm used to group similar data points into clusters.

Unlike supervised learning, we don't provide target labels.

---

🔍 What is Unsupervised Learning?

Unsupervised Learning works with data that has no predefined labels.

The model tries to discover:

- 🔹 Patterns
- 🔹 Groups
- 🔹 Similarities
- 🔹 Hidden structures

Example

A shopping company has customer information but doesn't know the customer types.

K-Means can discover groups such as:

🛍️ High-value Customers
💰 Budget Customers
👨‍💼 Regular Customers

---

⚙️ How K-Means Works

K-Means follows these basic steps:

1️⃣ Choose K

Decide how many clusters we want.

Example:

K = 3

2️⃣ Initialize Centroids

The algorithm selects initial cluster centers called centroids.

3️⃣ Assign Data Points

Each data point is assigned to the nearest centroid.

4️⃣ Update Centroids

The centroid is recalculated based on the points belonging to that cluster.

5️⃣ Repeat

The process continues until the clusters become stable.

---

📌 Important Terms

Term| Meaning
K| Number of clusters
Cluster| Group of similar data points
Centroid| Center of a cluster
Inertia| Measure of within-cluster distance
Elbow Method| Technique to choose K

---

📊 Choosing the Value of K

One common technique is the Elbow Method.

We calculate the inertia for different values of K.

K = 1 → Inertia
K = 2 → Inertia
K = 3 → Inertia
K = 4 → Inertia
...

We look for the point where adding more clusters gives only a small improvement.

That point is called the Elbow.

---

📏 Why Feature Scaling Matters

K-Means uses distance to assign points to clusters.

If one feature has a much larger scale than another, it can dominate the distance calculation.

Therefore, we often use:

StandardScaler()

before applying K-Means.

---

🛠️ Libraries Used

numpy
pandas
matplotlib
scikit-learn

Important classes:

KMeans
StandardScaler
silhouette_score

---

💻 Projects Practiced

🔹 Project 1 — K-Means Basics

File:

kmeans_basics.py

Learned how to:

- Create sample data
- Apply K-Means
- Create clusters
- Find cluster centers
- Display cluster assignments

🔹 Project 2 — Customer Segmentation

File:

customer_clustering.py

Used customer data such as:

- Annual Income
- Spending Score

Goal:

«Group customers with similar purchasing behavior.»

---

📈 Evaluation

Unlike classification, K-Means doesn't use accuracy because there are no predefined target labels.

Instead, we can use:

🔹 Inertia

Measures how close points are to their cluster centers.

🔹 Silhouette Score

Measures how well-separated the clusters are.

A higher silhouette score generally indicates better-defined clusters.

---

🌍 Real-World Applications

K-Means is used in:

- 🛒 Customer segmentation
- 🎯 Marketing
- 🛍️ Recommendation systems
- 🏥 Patient grouping
- 🖼️ Image compression
- 📊 Data analysis
- 💳 Customer behavior analysis

---

🧠 Key Takeaways

✔ K-Means is an Unsupervised Learning algorithm
✔ It groups similar data points
✔ K represents the number of clusters
✔ Centroids represent cluster centers
✔ Distance is used to assign points
✔ Feature scaling is important
✔ Elbow Method helps choose K
✔ Inertia helps evaluate clustering

---

📊 180-DAY AI JOURNEY

Progress: 23 / 180

█████░░░░░░░░░░░░░░░ 12.78%

✅ Completed

- Day 01 — AI Fundamentals
- Day 02 — NumPy
- Day 03 — NumPy Operations
- Day 04 — Pandas
- Day 05 — Data Cleaning
- Day 06 — Data Visualization
- Day 07 — Statistics
- Day 08 — Probability
- Day 09 — EDA
- Day 10 — Machine Learning Introduction
- Day 11 — Linear Regression
- Day 12 — Train/Test Split
- Day 13 — Multiple Linear Regression
- Day 14 — Logistic Regression
- Day 15 — Model Evaluation
- Day 16 — Decision Trees
- Day 17 — Random Forest
- Day 18 — KNN
- Day 19 — SVM
- Day 20 — Naive Bayes
- Day 21 — Model Comparison
- Day 22 — Cross-Validation & Hyperparameter Tuning
- Day 23 — K-Means Clustering ⭐

🔜 Next

Day 24 — Hierarchical Clustering 🌳

---

🔥 Today's Goal

«Learn → Code → Experiment → Commit → Push → Repeat»

Another step completed in my 180 Days of AI Journey! 🚀🤖

#AI #MachineLearning #KMeans #UnsupervisedLearning #Python #DataScience #LearningInPublic #180DaysOfAI #GitHub
