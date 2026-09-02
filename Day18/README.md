✦ DAY 18 — K-NEAREST NEIGHBORS (KNN) ✦

<div align="center">👥 Learning From Nearby Data

180 DAYS OF AI • DAY 18 / 180

Today I learned how a machine can make predictions by looking at similar examples.

</div>---

🌱 Today's Focus

Today I learned about K-Nearest Neighbors (KNN).

KNN is a supervised Machine Learning algorithm mainly used for:

- 🎯 Classification
- 📈 Regression

Its basic idea is simple:

«Look at the nearest data points and use them to make a prediction.»

---

🧠 How KNN Works

Suppose we want to predict whether a student will pass.

The model looks at students with similar:

📚 Study Hours
📊 Previous Marks

Then it checks their outcomes.

        👤 New Student
              ↓
     Find nearest students
              ↓
      👥 👥 👥 👥 👥
              ↓
       🗳️ Majority Vote
              ↓
          🎓 PASS

---

🔢 What Does "K" Mean?

"K" represents the number of nearest neighbors considered.

For example:

K = 3

The algorithm looks at the 3 nearest data points.

If:

Neighbor 1 → PASS
Neighbor 2 → PASS
Neighbor 3 → FAIL

The majority is:

PASS 🎉

So the model predicts PASS.

---

📏 Distance

KNN needs a way to determine which data points are closest.

A common method is Euclidean Distance.

For two points:

(x₁, y₁)
(x₂, y₂)

the distance is:

√((x₂-x₁)² + (y₂-y₁)²)

Smaller distance means the points are more similar according to the chosen features.

---

⚖️ Feature Scaling

KNN is sensitive to the scale of features because it relies on distance.

For example:

Age → 18–25
Income → 20,000–100,000

Income has much larger numerical values and could dominate the distance calculation.

So feature scaling is often important.

Today I practiced:

StandardScaler

to standardize the features.

---

🎯 Choosing K

The value of "K" can affect the model.

Small K

- More sensitive to individual data points
- Can be affected by noise

Large K

- More stable
- Can become too general

Therefore, choosing an appropriate "K" is important.

---

🆚 KNN vs Decision Tree

KNN 👥| Decision Tree 🌳
Uses nearby data points| Uses decision rules
Distance-based| Split-based
Scaling is often important| Scaling usually isn't required
Simple concept| Easy to interpret
Prediction can be slower with large datasets| Usually faster at prediction

---

💻 Today's Projects

01 — KNN Basics 👥

Built a KNN classifier to predict student outcomes.

02 — Student KNN Predictor 🎓

Used:

- Study Hours
- Attendance
- Previous Marks

to predict:

PASS / FAIL

---

🛠️ Tech Stack

"Python" • "NumPy" • "Scikit-learn" • "KNN" • "StandardScaler" • "Machine Learning"

---

📂 Files

Day-18/
│
├── README.md
├── knn_basics.py
└── student_knn.py

---

📈 Journey Progress

DAY 18 / 180

██████████████████░░

10.00% COMPLETE 🚀

🎉 10% OF THE JOURNEY COMPLETED!

18 days of learning.

One algorithm at a time.

One project at a time.

One step closer to becoming an AI/ML developer. 🤖

---

💭 Today's Thought

«"Sometimes the best way to understand something new is to look at what is already similar." 👥🧠»

---

<div align="center">✨ DAY 18 COMPLETED ✨

Find → Compare → Vote → Predict 🔁

Next → Day 19 🚀

</div>#180DaysOfAI #Day18 #KNN #MachineLearning #Python #ScikitLearn #AI #ArtificialIntelligence #AIJourney
