✦ DAY 20 — NAIVE BAYES 🧠 ✦

<div align="center">🧠 Predicting With Probability

180 DAYS OF AI • DAY 20 / 180

Today I learned how probability can be used to classify data.

</div>---

🌱 Today's Focus

Today I learned about Naive Bayes, a supervised Machine Learning algorithm based on Bayes' Theorem.

It is commonly used for classification problems.

Some real-world applications are:

📧 Spam Detection
📝 Text Classification
😊 Sentiment Analysis
📰 News Classification
📄 Document Classification

---

🧠 What is Naive Bayes?

Naive Bayes predicts the probability of a class based on the available features.

It is called "Naive" because it assumes that the features are conditionally independent given the class.

The assumption is often not perfectly true in real-world data, but the algorithm can still perform surprisingly well.

---

📐 Bayes' Theorem

The basic formula is:

                P(B | A) × P(A)
P(A | B) = ─────────────────────
                  P(B)

Where:

- "P(A | B)" → Probability of A given B
- "P(B | A)" → Probability of B given A
- "P(A)" → Prior probability
- "P(B)" → Evidence

---

📧 Real-World Example — Spam Detection

Imagine receiving an email:

"Congratulations! You won a FREE prize!"

The model looks at words such as:

FREE
WIN
PRIZE
CONGRATULATIONS

It compares these patterns with previously labeled emails.

Email
  ↓
Extract Features
  ↓
Calculate Probabilities
  ↓
🤖 Naive Bayes
  ↓
SPAM / NOT SPAM

---

🔑 Important Concepts

1️⃣ Prior Probability

The probability of a class before considering the current features.

2️⃣ Likelihood

How likely the observed features are for a particular class.

3️⃣ Posterior Probability

The updated probability after considering the evidence.

4️⃣ Conditional Independence

Naive Bayes assumes that features are conditionally independent given the class.

---

🧩 Types of Naive Bayes

Scikit-learn provides several variants.

GaussianNB

Useful when features are continuous and can reasonably be modeled using Gaussian distributions.

MultinomialNB

Commonly used for discrete counts such as word frequencies.

BernoulliNB

Useful when features are binary, such as whether a word appears or not.

---

🆚 SVM vs Naive Bayes

SVM ⚡| Naive Bayes 🧠
Margin-based| Probability-based
Finds a decision boundary| Uses Bayes' theorem
Can use kernels| Uses probability distributions
Often needs feature scaling| Scaling is generally not required
Strong for many classification tasks| Very useful for text classification

---

💻 Today's Projects

01 — Naive Bayes Basics

Built a Gaussian Naive Bayes classifier using numerical data.

02 — Spam Detector 📧

Built a simple text classification model using:

- "CountVectorizer"
- "MultinomialNB"

to classify messages as:

SPAM / NOT SPAM

---

🛠️ Tech Stack

"Python" • "NumPy" • "Scikit-learn" • "Naive Bayes" • "NLP Basics" • "Machine Learning"

---

📂 Files

Day-20/
│
├── README.md
├── naive_bayes_basics.py
└── spam_detector.py

---

📈 Journey Progress

DAY 20 / 180

████████████████████░

11.11% COMPLETE 🚀

🎉 20 DAYS COMPLETED!

I've now explored several important classification algorithms:

Logistic Regression 🎯
        ↓
Decision Tree 🌳
        ↓
Random Forest 🌲
        ↓
KNN 👥
        ↓
SVM ⚡
        ↓
Naive Bayes 🧠

---

💭 Today's Thought

«"AI can turn simple probabilities into powerful decisions." 🧠📊»

---

<div align="center">✨ DAY 20 COMPLETED ✨

Features → Probability → Classification → Decision 🔁

Next → Day 21 🚀

</div>#180DaysOfAI #Day20 #NaiveBayes #MachineLearning #Python #NLP #SpamDetection #ScikitLearn #AI #ArtificialIntelligence #AIJourney
