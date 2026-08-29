✦ DAY 14 — LOGISTIC REGRESSION ✦

<div align="center">🎯 From Predicting Numbers to Predicting Categories

180 DAYS OF AI • DAY 14 / 180

Today I learned my first classification algorithm.

</div>---

🌱 Today's Focus

Until now, I mainly worked with Regression, where the model predicts a continuous numerical value.

Today, I entered the world of:

🎯 CLASSIFICATION

Classification is used when the output belongs to a category.

Examples:

📧 Spam / Not Spam
❤️ Disease / No Disease
🎓 Pass / Fail
🛒 Buy / Don't Buy
🐱 Cat / Dog

---

🧠 What is Logistic Regression?

Despite its name, Logistic Regression is primarily a classification algorithm.

It estimates the probability that an observation belongs to a class.

For example:

Study Hours = 6
       ↓
🤖 Logistic Regression
       ↓
Probability of Passing = 91%
       ↓
🎓 PASS

---

📈 Probability → Class

The model produces a probability between "0" and "1".

For binary classification, a common decision rule is:

Probability ≥ 0.5 → Class 1
Probability < 0.5 → Class 0

Example:

0.85 → PASS
0.32 → FAIL

The threshold can be changed depending on the problem.

---

🔄 Regression vs Classification

Regression| Classification
Predicts numbers| Predicts categories
House price| Spam / Not Spam
Temperature| Pass / Fail
Salary| Yes / No
Linear Regression| Logistic Regression

---

🧩 Important Concepts

Today I practiced:

- Classification
- Binary classification
- Logistic Regression
- Training data
- Testing data
- Probabilities
- Predictions
- Accuracy
- Confusion Matrix

---

📊 Confusion Matrix

A confusion matrix helps us understand classification results.

                    Predicted
                 Positive  Negative
Actual Positive     TP        FN
Actual Negative     FP        TN

Where:

- TP → True Positive
- TN → True Negative
- FP → False Positive
- FN → False Negative

---

💻 Today's Projects

01 — Logistic Regression Basics 🎯

Built a classification model to predict whether a student will pass based on study hours.

02 — Student Pass Predictor 🎓

Created a practical model using:

- Study hours
- Attendance
- Previous performance

to predict Pass / Fail.

---

🛠️ Tech Stack

"Python" • "NumPy" • "Pandas" • "Scikit-learn" • "Machine Learning"

---

📂 Files

Day-14/
│
├── README.md
├── logistic_regression.py
└── student_pass_prediction.py

---

📈 Journey Progress

DAY 14 / 180

██████████████░░░░░░

7.78% COMPLETE 🚀

---

💭 Today's Thought

«"Prediction isn't always about a number. Sometimes, it's about making the right decision." 🎯»

---

<div align="center">✨ DAY 14 COMPLETED ✨

Data → Train → Probability → Classification → Evaluate 🔁

Next → Day 15 🚀

</div>#180DaysOfAI #Day14 #LogisticRegression #Classification #MachineLearning #Python #ScikitLearn #ArtificialIntelligence #AIJourney
