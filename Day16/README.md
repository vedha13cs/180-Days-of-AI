✦ DAY 16 — DECISION TREES 🌳 ✦

<div align="center">🌳 Learning Through Decisions

180 DAYS OF AI • DAY 16 / 180

Today I learned how machines can make decisions step by step.

</div>---

🌱 Today's Focus

Today I learned about the Decision Tree Machine Learning algorithm.

A Decision Tree makes predictions by asking a sequence of questions about the data.

It works similar to:

IF this condition is true
        ↓
    Go this way
ELSE
        ↓
    Go another way

---

🧠 What is a Decision Tree?

A Decision Tree is a supervised Machine Learning algorithm that can be used for:

- 🎯 Classification
- 📈 Regression

For classification, it predicts categories such as:

PASS / FAIL
SPAM / NOT SPAM
YES / NO

---

🌳 How Does It Work?

Imagine predicting whether a student will pass:

              Study Hours > 4?
                 /        \
               YES         NO
               /             \
       Attendance > 75?      FAIL
          /       \
        YES        NO
        /           \
      PASS          FAIL

The model keeps splitting the data using useful features until it reaches a prediction.

---

🔑 Important Terms

🌱 Root Node

The first decision in the tree.

🔀 Decision Node

A point where the model makes a decision.

🍃 Leaf Node

The final prediction.

↔️ Branch

The path connecting decisions.

---

📊 Gini Impurity

For classification, Decision Trees can use Gini Impurity to determine how well a split separates the classes.

A lower impurity generally means a better separation.

---

⚠️ Overfitting

A Decision Tree can become too complex and memorize the training data.

This is called:

«Overfitting»

To control it, we can use parameters such as:

max_depth
min_samples_split
min_samples_leaf

---

💻 Today's Projects

01 — Decision Tree Basics 🌳

Built a simple Decision Tree classifier using student data.

02 — Student Pass Predictor 🎓

Used:

- Study Hours
- Attendance
- Previous Marks

to predict whether a student will Pass or Fail.

---

🛠️ Tech Stack

"Python" • "NumPy" • "Scikit-learn" • "Decision Tree" • "Machine Learning"

---

📂 Files

Day-16/
│
├── README.md
├── decision_tree_basics.py
└── student_decision_tree.py

---

📈 Journey Progress

DAY 16 / 180

████████████████░░░░

8.89% COMPLETE 🚀

---

💭 Today's Thought

«"Complex problems can become simple when we break them into smaller decisions." 🌳🧠»

---

<div align="center">✨ DAY 16 COMPLETED ✨

Question → Decision → Branch → Prediction 🔁

Next → Day 17 🚀

</div>#180DaysOfAI #Day16 #DecisionTree #MachineLearning #Python #ScikitLearn #AI #ArtificialIntelligence #AIJourney
