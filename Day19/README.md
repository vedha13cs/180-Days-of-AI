✦ DAY 19 — SUPPORT VECTOR MACHINES (SVM) ⚡ ✦

<div align="center">⚡ Finding the Best Boundary

180 DAYS OF AI • DAY 19 / 180

Today I learned how Machine Learning models can separate different classes using an optimal decision boundary.

</div>---

🌱 Today's Focus

Today I learned about Support Vector Machines (SVM).

SVM is a supervised Machine Learning algorithm commonly used for:

- 🎯 Classification
- 📈 Regression

The main goal of SVM is to find the best decision boundary between different classes.

---

🧠 What is SVM?

Imagine that we have two groups of data:

🔵 🔵 🔵        🟠 🟠 🟠
🔵 🔵 🔵        🟠 🟠 🟠
🔵 🔵 🔵        🟠 🟠 🟠

SVM tries to find a boundary that separates them:

🔵 🔵 🔵   |   🟠 🟠 🟠
🔵 🔵 🔵   |   🟠 🟠 🟠
🔵 🔵 🔵   |   🟠 🟠 🟠
            ↑
       Decision Boundary

But SVM doesn't just find any boundary.

It tries to find a boundary with a large margin between the classes.

---

📏 What is a Margin?

The margin is the distance between the decision boundary and the closest data points from each class.

Class A        Margin        Class B

🔵 🔵     |      |      |     🟠 🟠
          ←──────→
             ↑
          Boundary

SVM tries to maximize this margin.

A larger margin can help the model generalize better to unseen data.

---

⭐ Support Vectors

The data points closest to the decision boundary are called:

«Support Vectors»

They are important because they influence the position of the decision boundary.

🔵 🔵 ⭐       |       ⭐ 🟠 🟠
              ↑
         Decision Boundary

⭐ = Support Vector

---

⚙️ Important SVM Parameters

"C"

Controls the trade-off between:

- A wider margin
- Classification errors

"kernel"

Defines how the model handles the relationship between data points.

Common kernels include:

linear
rbf
poly

"gamma"

For certain kernels such as RBF, gamma controls how strongly individual training examples influence the decision boundary.

---

🔄 Feature Scaling

SVM is sensitive to feature scale.

So scaling is often important before training.

Today I used:

StandardScaler

to standardize the features.

---

🧩 Linear vs Non-Linear Data

Some datasets can be separated with a straight line:

🔵 🔵 🔵 | 🟠 🟠 🟠

This is a linear decision boundary.

Other datasets have more complicated patterns.

For these cases, kernels such as RBF can help SVM create a non-linear decision boundary.

---

🆚 SVM vs KNN

SVM ⚡| KNN 👥
Learns a decision boundary| Uses nearby data points
Margin-based| Distance-based
Scaling is important| Scaling is important
Can use kernels| No kernel concept
Strong for many classification problems| Simple and intuitive

---

💻 Today's Projects

01 — SVM Basics ⚡

Built an SVM classifier using student data.

02 — Student Performance Predictor 🎓

Used:

- Study Hours
- Attendance
- Previous Marks

to predict:

PASS / FAIL

The model was evaluated using:

- Accuracy
- Confusion Matrix
- Classification Report

---

🛠️ Tech Stack

"Python" • "NumPy" • "Scikit-learn" • "SVM" • "StandardScaler" • "Machine Learning"

---

📂 Files

Day-19/
│
├── README.md
├── svm_basics.py
└── student_svm.py

---

📈 Journey Progress

DAY 19 / 180

███████████████████░

10.56% COMPLETE 🚀

🎉 19 DAYS COMPLETED!

My Machine Learning foundation is growing:

Regression
    ↓
Classification
    ↓
Logistic Regression
    ↓
Decision Tree
    ↓
Random Forest
    ↓
KNN
    ↓
SVM ⚡

---

💭 Today's Thought

«"The goal isn't just to separate the data — it's to find a boundary that generalizes well." ⚡🧠»

---

<div align="center">✨ DAY 19 COMPLETED ✨

Data → Boundary → Margin → Classification 🔁

Next → Day 20 🚀

</div>#180DaysOfAI #Day19 #SVM #SupportVectorMachine #MachineLearning #Python #ScikitLearn #AI #ArtificialIntelligence #AIJourney
