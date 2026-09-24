🧠 Day 35/180 — Named Entity Recognition (NER)

«Turning raw text into meaningful information! 🔍✨»

Welcome to Day 35 of my 180 Days of AI Learning Journey 🚀

Today, I explored Named Entity Recognition (NER) — an important Natural Language Processing (NLP) technique that helps computers identify important entities such as people, organizations, locations, dates, and money from text.

---

🎯 Today's Goal

By the end of today, I learned:

- 🔹 What is Named Entity Recognition?
- 🔹 How NER works
- 🔹 Common entity types
- 🔹 How to perform NER using Python
- 🔹 How NLP models identify entities from sentences
- 🔹 Real-world applications of NER

---

🤔 What is Named Entity Recognition?

Named Entity Recognition (NER) is an NLP technique used to identify and classify important information in text.

For example:

Vedhavathi joined Google in Bengaluru in 2026.

An NER model can identify:

Vedhavathi → PERSON
Google → ORG
Bengaluru → GPE
2026 → DATE

So instead of treating the entire sentence as plain text, the model extracts useful information from it.

---

🧩 Common Entity Types

Entity| Meaning| Example
PERSON| Person's name| Vedhavathi
ORG| Organization| Google
GPE| Country/City/State| India
DATE| Date| 24 September 2026
MONEY| Monetary value| ₹5 lakh
EVENT| Event| Olympics
PRODUCT| Product| iPhone
LOC| Location| Indian Ocean

---

⚙️ How NER Works

A simple NER pipeline looks like this:

Raw Text
   ↓
Tokenization
   ↓
Language Model
   ↓
Entity Detection
   ↓
Entity Classification
   ↓
Named Entities

Example:

"Apple opened a new office in Bengaluru."

The model identifies:

Apple      → ORG
Bengaluru  → GPE

---

🐍 Python & spaCy

For today's practice, I used spaCy, a popular Python NLP library.

Install spaCy

pip install spacy

Download the English model

python -m spacy download en_core_web_sm

---

💻 Project Files

Day-35-Named-Entity-Recognition/
│
├── README.md
├── ner_basics.py
└── custom_ner.py

📌 "ner_basics.py"

This program:

- Loads a pre-trained NLP model
- Processes text
- Detects entities
- Displays entity names and labels

📌 "custom_ner.py"

This program uses a longer paragraph to identify multiple entities such as:

- 👤 People
- 🏢 Organizations
- 📍 Locations
- 📅 Dates
- 💰 Money

---

🌍 Real-World Applications

NER is used in many real-world AI systems.

📰 News Analysis

Extract:

People + Organizations + Locations + Events

from news articles.

🔎 Search Engines

NER helps understand whether a search term refers to:

Person
Place
Company
Product

💬 Chatbots

Chatbots can identify important information from user messages.

📄 Resume Processing

NER can help extract:

Name
Skills
Company
Education
Location

🏥 Healthcare

NER can identify entities such as:

Diseases
Medicines
Hospitals
Doctors
Medical Terms

---

🧠 Example

Input:

Sundar Pichai is the CEO of Google and works in California.

Possible entities:

Sundar Pichai → PERSON
Google        → ORG
California    → GPE

This converts unstructured text into structured information.

---

⚠️ Challenges in NER

NER is powerful, but it is not perfect.

Some challenges include:

- 🔹 Ambiguous names
- 🔹 Spelling mistakes
- 🔹 Unknown words
- 🔹 Different languages
- 🔹 Context-dependent meanings
- 🔹 Sarcasm and informal text
- 🔹 Same word having different meanings

For example:

Apple

could refer to:

🍎 Fruit
🏢 Apple Inc.

The surrounding context is important.

---

🆚 NER vs Text Classification

NER| Text Classification
Finds entities| Classifies complete text
Extracts specific information| Assigns a category
Example: Google → ORG| Example: Review → Positive
Used for information extraction| Used for prediction

---

📝 Practice Tasks

Try these yourself:

Practice 1

Create a sentence containing:

Person + Company + Location

Run NER and identify the entities.

Practice 2

Write a sentence containing:

Date + Money + Organization

Check whether the model detects them.

Practice 3

Create your own paragraph about a college event and extract:

People
Organizations
Locations
Dates

---

💡 What I Learned Today

«NER taught me how AI can look at ordinary sentences and extract meaningful information from them.»

I learned that NLP is not only about understanding words — it is also about understanding what those words represent.

---

📈 My AI Journey Progress

Day 35 / 180
███████░░░░░░░░░░░░░ 19.44%

✅ Completed

- Day 1 → AI Fundamentals
- Day 2 → NumPy
- Day 3 → NumPy Operations
- Day 4 → Pandas
- Day 5 → Data Cleaning
- Day 6 → Data Visualization
- Day 7 → Statistics
- Day 8 → Probability
- Day 9 → EDA
- Day 10 → Machine Learning Introduction
- Day 11 → Linear Regression
- Day 12 → Train/Test Split
- Day 13 → Multiple Linear Regression
- Day 14 → Logistic Regression
- Day 15 → Model Evaluation
- Day 16 → Decision Trees
- Day 17 → Random Forest
- Day 18 → KNN
- Day 19 → SVM
- Day 20 → Naive Bayes
- Day 21 → Model Comparison
- Day 22 → Cross-Validation & Hyperparameter Tuning
- Day 23 → K-Means Clustering
- Day 24 → Hierarchical Clustering
- Day 25 → DBSCAN
- Day 26 → PCA & Dimensionality Reduction
- Day 27 → Association Rule Learning
- Day 28 → Recommendation Systems
- Day 29 → NLP Fundamentals
- Day 30 → Text Preprocessing
- Day 31 → Bag of Words
- Day 32 → TF-IDF
- Day 33 → Sentiment Analysis
- Day 34 → NLP Text Classification
- Day 35 → Named Entity Recognition 🎯

---

🔥 35 Days Completed!

145 Days Remaining!

One concept at a time.
One program at a time.
One day at a time.

«Consistency over motivation. 💻🔥»

---

🚀 Next Step

Coming next:

Day 36 → Continuing NLP & Advanced Text Representation

The journey continues... 🌱🤖

---

⭐ If you find this journey interesting

Feel free to explore the repository and follow along with my 180 Days of AI Learning Journey.

Learning → Practicing → Building → Improving 🚀
