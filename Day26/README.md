📉 DAY 26/180 — PCA & DIMENSIONALITY REDUCTION

«“Less data doesn't always mean less information — sometimes it means finding what matters most.” 🧠»

---

🌱 Today's Learning

Today I learned about Dimensionality Reduction and one of its most important techniques:

🔵 PCA — Principal Component Analysis

PCA is a technique used to reduce the number of features in a dataset while trying to preserve the most important information.

---

🧠 What is Dimensionality?

A dimension can be thought of as a feature or variable in our dataset.

For example:

Student Dataset

Age
Study Hours
Attendance
Previous Marks
Assignments
Sleep Hours

Here we have 6 features.

So the dataset has 6 dimensions.

---

📉 What is Dimensionality Reduction?

Dimensionality Reduction means reducing the number of features while keeping as much useful information as possible.

Example:

6 Features
    ↓
   PCA
    ↓
2 Principal Components

This can make data:

- Easier to visualize
- Faster to process
- Less complex
- Less affected by redundant features

---

🔵 What is PCA?

Principal Component Analysis (PCA) transforms the original features into new variables called Principal Components.

The first components try to capture the greatest amount of variation in the data.

Original Features
       ↓
      PCA
       ↓
Principal Components
       ↓
Reduced Dataset

---

📌 Principal Components

PCA creates new components such as:

PC1
PC2
PC3
...

🔹 PC1

Captures the largest amount of variance.

🔹 PC2

Captures the next largest amount of variance while being independent/orthogonal to PC1.

---

📊 Explained Variance

One important concept in PCA is:

"explained_variance_ratio_"

It tells us how much of the dataset's variance is captured by each principal component.

Example:

PC1 → 60%
PC2 → 25%
PC3 → 10%
PC4 → 5%

If we use PC1 + PC2:

60% + 25% = 85%

So two components preserve approximately 85% of the variance.

---

⚙️ PCA Workflow

Collect Data
     ↓
Clean Data
     ↓
Scale Features
     ↓
Apply PCA
     ↓
Select Components
     ↓
Transform Data
     ↓
Analyze / Visualize

---

📏 Why Feature Scaling?

PCA is sensitive to the scale of features.

Suppose:

Age       → 18–60
Salary    → 20,000–1,00,000

The larger-scale feature can dominate the analysis.

Therefore, we commonly standardize the data first:

StandardScaler()

---

💻 Today's Practice

🔹 01 — PCA Basics

File:

pca_basics.py

Practiced:

- Creating a dataset
- Standardizing features
- Applying PCA
- Reducing dimensions
- Checking explained variance

---

🔹 02 — PCA Visualization

File:

pca_visualization.py

Practiced reducing a dataset to 2 dimensions so that it can be visualized more easily.

---

🌍 Real-World Applications

PCA can be useful for:

🖼️ Image compression
📊 Data visualization
🧬 Biological data analysis
🤖 Machine Learning preprocessing
📈 Feature reduction
🔍 Pattern discovery
📱 High-dimensional data analysis

---

🆚 Feature Selection vs PCA

Feature Selection

Selects existing features.

Age
Income
Marks

Some features are removed.

PCA

Creates new features called principal components.

PC1
PC2
PC3

So PCA is a feature transformation technique, not simply feature deletion.

---

🧠 KEY TAKEAWAYS

✔ PCA stands for Principal Component Analysis

✔ PCA is used for dimensionality reduction

✔ Dimensions can represent features

✔ PCA creates principal components

✔ PC1 captures the largest variance

✔ explained_variance_ratio_ shows captured variance

✔ Feature scaling is important before PCA

✔ PCA can help visualize high-dimensional data

✔ PCA can reduce complexity while retaining important information

---

📊 MY 180-DAY AI JOURNEY

🔥 Progress: 26 / 180

█████░░░░░░░░░░░░░░░ 14.44%

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
⭐ Day 26 → PCA & Dimensionality Reduction

🔜 NEXT

Day 27 → Association Rule Learning 🛒

---

💭 Today's Reflection

Today I understood that datasets can contain many features, but not every feature needs to remain in its original form.

PCA helps us transform complex, high-dimensional data into a smaller representation while preserving important variation.

26 days completed.
154 days to go. 🚀

---

«“Consistency over motivation.”»

#AI #MachineLearning #PCA #DimensionalityReduction #Python #DataScience #LearningInPublic #180DaysOfAI #GitHub
