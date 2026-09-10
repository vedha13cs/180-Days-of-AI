🚀 DAY 23/180 — K-MEANS CLUSTERING

«“AI doesn't always need answers. Sometimes, it discovers the groups on its own.” 🤖»

---

🌱 Today's Learning

Today I entered the world of Unsupervised Learning and learned about K-Means Clustering.

K-Means is an algorithm that helps machines find groups of similar data points without predefined labels.

---

🧠 What is Unsupervised Learning?

In supervised learning, we provide the model with:

Input → Output

But in unsupervised learning, we provide only the data.

Input → AI discovers patterns

The model tries to identify hidden structures and groups within the data.

---

🔵 What is K-Means?

K-Means Clustering divides data into a specified number of groups called clusters.

For example, a shopping company may have thousands of customers.

K-Means can help identify:

🛍️ High Spending Customers
💰 Medium Spending Customers
🪙 Low Spending Customers

without manually labeling every customer.

---

⚙️ How K-Means Works

1️⃣ Choose K

First, we decide how many clusters we want.

Example:

K = 3

This means we want 3 groups.

2️⃣ Select Initial Centroids

The algorithm chooses initial points as the centers of the clusters.

These centers are called centroids.

3️⃣ Assign Data Points

Each data point is assigned to the nearest centroid.

4️⃣ Calculate New Centroids

The algorithm calculates a new center for each cluster.

5️⃣ Repeat

The assignment and centroid calculation continue until the clusters become stable.

---

📌 Important Terms

🔹 K

Number of clusters.

🔹 Cluster

A group of similar data points.

🔹 Centroid

The center point of a cluster.

🔹 Inertia

Measures how close data points are to their cluster centers.

🔹 Elbow Method

A method used to help select a suitable value of K.

---

📊 Choosing K — Elbow Method

We can test different values:

K = 1
K = 2
K = 3
K = 4
K = 5
...

For each K, we calculate the inertia.

As K increases, inertia generally decreases.

We look for the point where the decrease starts becoming less significant.

That point is called the Elbow.

---

📏 Why Scaling is Important

K-Means is based on distance.

Suppose we have:

Age       → 18–60
Income    → 10,000–10,00,000

Income has a much larger numerical scale.

It could therefore have too much influence on the distance calculation.

So we commonly use:

StandardScaler()

before clustering.

---

💻 Today's Practice

🔹 Program 1 — K-Means Basics

"kmeans_basics.py"

I practiced:

- Creating sample data
- Creating a K-Means model
- Choosing the number of clusters
- Training the model
- Getting cluster labels
- Finding centroids
- Predicting clusters for new data

🔹 Program 2 — Customer Segmentation

"customer_clustering.py"

I created a simple customer dataset using:

- Annual Income
- Spending Score

Then I used K-Means to divide customers into groups.

---

🌍 Real-World Applications

K-Means can be used for:

- 🛒 Customer segmentation
- 📢 Marketing analysis
- 🎯 Targeted advertising
- 🏥 Patient grouping
- 🖼️ Image compression
- 🛍️ Shopping behavior analysis
- 📊 Pattern discovery

---

🧪 Model Evaluation

Since K-Means does not have predefined target labels, accuracy is generally not the appropriate metric.

Instead, we can use:

🔹 Inertia

Lower inertia means points are closer to their cluster centers.

🔹 Silhouette Score

It measures how well-separated the clusters are.

A higher silhouette score generally indicates better-defined clusters.

---

🧠 What I Learned

✔ What Unsupervised Learning means
✔ What K-Means Clustering is
✔ How clusters are created
✔ What centroids are
✔ How K is selected
✔ Elbow Method
✔ Inertia
✔ Silhouette Score
✔ Why feature scaling matters
✔ Customer segmentation using K-Means

---

📈 MY 180-DAY AI JOURNEY

🔥 Progress

23 / 180 Days

█████░░░░░░░░░░░░░░░ 12.78%

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
Day 23 → K-Means Clustering ⭐

🔜 NEXT

Day 24 → Hierarchical Clustering 🌳

---

💭 Today's Reflection

Today I learned that machine learning doesn't always require labeled answers.

Sometimes, the goal is simply to discover patterns hidden inside the data.

One more concept learned.

One more step forward.

23 days down. 157 days to go. 🚀

---

🔥 KEEP LEARNING. KEEP BUILDING. KEEP MOVING.

«“Consistency over motivation.”»

#AI #MachineLearning #Python #KMeans #UnsupervisedLearning #DataScience #LearningJourney #180DaysOfAI #GitHub
