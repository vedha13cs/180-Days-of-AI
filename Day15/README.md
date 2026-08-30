✦ DAY 15 — CLASSIFICATION EVALUATION ✦

<div align="center">📊 Is My Classification Model Really Good?

180 DAYS OF AI • DAY 15 / 180

Today I learned how to look beyond accuracy.

</div>---

🌱 Today's Focus

Yesterday, I built my first Logistic Regression classification model.

Today, I learned how to measure its performance using different evaluation metrics.

A model predicting:

PASS / FAIL
SPAM / NOT SPAM
YES / NO

needs to be evaluated carefully.

---

🧠 The Four Important Metrics

🎯 01 — Accuracy

Accuracy tells us the percentage of predictions that were correct.

Accuracy =
Correct Predictions
────────────────────
Total Predictions

Example:

90 correct predictions
out of 100

Accuracy = 90%

---

🎯 02 — Precision

Precision answers:

«"When the model predicts Positive, how often is it actually Positive?"»

Precision =
TP
────────────
TP + FP

High precision means fewer False Positives.

---

🔍 03 — Recall

Recall answers:

«"Of all the actual Positive cases, how many did the model find?"»

Recall =
TP
────────────
TP + FN

High recall means fewer False Negatives.

---

⚖️ 04 — F1 Score

F1 Score combines Precision and Recall.

F1 = 2 × (Precision × Recall)
     ─────────────────────────
       Precision + Recall

It is useful when we want a balance between precision and recall.

---

🔲 Confusion Matrix

A confusion matrix shows four types of predictions:

                    PREDICTED
                 Positive  Negative
ACTUAL Positive    TP        FN
       Negative    FP        TN

🟢 TP — True Positive

Model predicted Positive and it was Positive.

🟢 TN — True Negative

Model predicted Negative and it was Negative.

🔴 FP — False Positive

Model predicted Positive but it was actually Negative.

🔴 FN — False Negative

Model predicted Negative but it was actually Positive.

---

🤖 Why This Matters in AI

Different applications care about different errors.

For example:

📧 Spam Detection
→ Precision can be important

🏥 Disease Screening
→ Recall can be extremely important

⚖️ Balanced Classification
→ F1 Score can be useful

So:

«A good model isn't always the model with the highest accuracy.»

---

💻 Today's Projects

01 — Classification Metrics

Created a Python program to calculate:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

02 — Student Model Evaluation 🎓

Evaluated a Logistic Regression model that predicts student Pass/Fail results.

---

🛠️ Tech Stack

"Python" • "NumPy" • "Scikit-learn" • "Logistic Regression" • "Machine Learning"

---

📂 Files

Day-15/
│
├── README.md
├── classification_metrics.py
└── student_model_evaluation.py

---

📈 Journey Progress

DAY 15 / 180

███████████████░░░░░

8.33% COMPLETE 🚀

🎉 15 DAYS COMPLETED!

I've now learned the basic workflow:

Data
 ↓
Clean
 ↓
Explore
 ↓
Train
 ↓
Predict
 ↓
Evaluate

---

💭 Today's Thought

«"A prediction is useful only when we know how much we can trust it." 🤖📊»

---

<div align="center">✨ DAY 15 COMPLETED ✨

Predict → Measure → Understand → Improve 🔁

Next → Day 16 🚀

</div>#180DaysOfAI #Day15 #MachineLearning #Classification #Precision #Recall #F1Score #Python #ScikitLearn #AIJourney
