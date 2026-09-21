📊 Day 31 — Bag of Words (BoW)

«🚀 180 Days of AI & Machine Learning Journey
Day 31/180 — Learning Bag of Words in NLP»

---

🌟 Today's Topic

Today I learned about Bag of Words (BoW), one of the basic techniques used in Natural Language Processing to convert text into numerical data.

Machine-learning models cannot directly understand sentences like humans.

For example:

"I love Python"

needs to be represented using numbers before a machine-learning model can work with it.

Bag of Words helps us perform this conversion by representing text based on the words that appear in it.

---

🧠 What is Bag of Words?

Bag of Words is a text representation technique that converts a collection of text documents into a numerical matrix based on word occurrence or frequency.

The basic idea is:

Text
  ↓
Find Words
  ↓
Create Vocabulary
  ↓
Count Word Occurrences
  ↓
Numerical Representation

BoW focuses on which words appear and how often they appear.

It does not understand the meaning or order of the words.

---

🔤 Simple Example

Suppose we have two sentences:

Document 1: "I love Python"
Document 2: "I love AI"

Step 1 — Create Vocabulary

Unique words:

I
love
Python
AI

Step 2 — Count the Words

Document| I| love| Python| AI
Document 1| 1| 1| 1| 0
Document 2| 1| 1| 0| 1

The text is now represented using numbers.

---

📚 Important Terms

1️⃣ Document

A single piece of text is called a document.

Example:

"I love Python"

---

2️⃣ Vocabulary

Vocabulary is the collection of unique words found across the documents.

Example:

["I", "love", "Python", "AI"]

---

3️⃣ Word Count

Word count represents how many times a particular word occurs in a document.

Example:

"I love AI and I love Python"

The word ""love"" appears:

2 times

---

4️⃣ Document-Term Matrix

A Document-Term Matrix represents documents using numerical word counts.

Example:

Document| AI| I| love| Python
Document 1| 0| 1| 1| 1
Document 2| 1| 1| 1| 0

Rows represent documents.

Columns represent words.

Values represent word counts.

---

🛠️ CountVectorizer

Scikit-learn provides a useful class called:

CountVectorizer

It automatically:

- Finds vocabulary
- Converts text into numerical features
- Counts word occurrences
- Creates a document-term matrix

Example:

from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "I love Python",
    "I love AI",
    "Python is powerful"
]

vectorizer = CountVectorizer()

bow_matrix = vectorizer.fit_transform(documents)

print(vectorizer.get_feature_names_out())
print(bow_matrix.toarray())

---

🔄 How "CountVectorizer" Works

Input Text
    ↓
CountVectorizer
    ↓
Tokenization
    ↓
Vocabulary Creation
    ↓
Word Counting
    ↓
Numerical Matrix

---

🤖 Using BoW for Machine Learning

Once text is converted into numbers, it can be given to a machine-learning model.

Example:

Text
 ↓
Bag of Words
 ↓
Numerical Features
 ↓
Machine Learning Model
 ↓
Prediction

For example, we can use BoW for:

- 😊 Sentiment analysis
- 📧 Spam detection
- 📰 Text classification
- 💬 Message classification

---

💻 Project 1 — Bag of Words Basics

File:

bag_of_words_basics.py

In this program, I practised:

- Creating text documents
- Creating vocabulary
- Using "CountVectorizer"
- Creating a Bag of Words matrix
- Understanding word counts

---

💻 Project 2 — Text Classification Using BoW

File:

text_classification_bow.py

In this program, I used:

- "CountVectorizer"
- Bag of Words
- "MultinomialNB"
- Text classification

Example:

"I love this movie"

can be classified as:

Positive

while:

"I hate this movie"

can be classified as:

Negative

---

🌍 Real-World Applications

Bag of Words can be used as a basic text representation technique in applications such as:

- 📧 Spam detection
- 😊 Sentiment analysis
- 📰 News classification
- 🔍 Search systems
- 💬 Message classification
- 📄 Document classification
- 🤖 Simple NLP applications

---

⚠️ Limitations of Bag of Words

Although BoW is simple and useful, it has some limitations.

1️⃣ Ignores Word Order

Consider:

"I love Python"

and:

"Python love I"

BoW may represent them similarly because it mainly considers word occurrence rather than sequence.

---

2️⃣ Does Not Understand Meaning

BoW does not actually understand the meaning of a sentence.

For example:

"I like Python"

and:

"I love Python"

contain different words even though their meanings are similar.

---

3️⃣ Large Vocabulary

If a dataset contains thousands or millions of unique words, the resulting matrix can become very large.

This can lead to:

- High memory usage
- Sparse matrices
- More computational requirements

---

4️⃣ Common Words Can Dominate

Very frequent words may appear many times without being especially useful for distinguishing documents.

This is one reason techniques such as TF-IDF are useful.

---

🆚 BoW vs TF-IDF

Bag of Words| TF-IDF
Uses word counts| Uses weighted word importance
Simple representation| More informative representation
Does not consider document importance| Considers how common a word is across documents
Easy to understand| Slightly more advanced

TF-IDF will be the next topic in my NLP journey. 🚀

---

🧪 Practice Tasks

- [x] Understand Bag of Words
- [x] Create a vocabulary
- [x] Count word occurrences
- [x] Understand document-term matrix
- [x] Use "CountVectorizer"
- [x] Convert text into numerical features
- [x] Use BoW with a classification model
- [x] Understand limitations of BoW

---

🔑 Key Takeaways

Bag of Words means:

«Representing text using the words that occur in the documents and their frequencies.»

The basic workflow is:

Text
 ↓
Vocabulary
 ↓
Word Counts
 ↓
Numerical Matrix
 ↓
Machine Learning

Today I understood how a computer can transform simple human language into numerical data that machine-learning algorithms can process.

---

📈 My AI Learning Progress

Day 31 / 180

███████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 17.22%

🔥 31 Days Completed
⏳ 149 Days Remaining

---

🗺️ Journey So Far

- ✅ Day 1 — AI Fundamentals
- ✅ Day 2 — NumPy
- ✅ Day 3 — NumPy Operations
- ✅ Day 4 — Pandas
- ✅ Day 5 — Data Cleaning
- ✅ Day 6 — Data Visualization
- ✅ Day 7 — Statistics
- ✅ Day 8 — Probability
- ✅ Day 9 — Exploratory Data Analysis
- ✅ Day 10 — Machine Learning Introduction
- ✅ Day 11 — Linear Regression
- ✅ Day 12 — Train/Test Split
- ✅ Day 13 — Multiple Linear Regression
- ✅ Day 14 — Logistic Regression
- ✅ Day 15 — Model Evaluation
- ✅ Day 16 — Decision Trees
- ✅ Day 17 — Random Forest
- ✅ Day 18 — K-Nearest Neighbors
- ✅ Day 19 — Support Vector Machines
- ✅ Day 20 — Naive Bayes
- ✅ Day 21 — Model Comparison
- ✅ Day 22 — Cross-Validation & Hyperparameter Tuning
- ✅ Day 23 — K-Means Clustering
- ✅ Day 24 — Hierarchical Clustering
- ✅ Day 25 — DBSCAN Clustering
- ✅ Day 26 — PCA & Dimensionality Reduction
- ✅ Day 27 — Association Rule Learning
- ✅ Day 28 — Recommendation Systems
- ✅ Day 29 — NLP Fundamentals
- ✅ Day 30 — Text Preprocessing
- ✅ Day 31 — Bag of Words

---

🔜 Next Step

Day 32 — TF-IDF

Next, I will learn how TF-IDF (Term Frequency–Inverse Document Frequency) assigns importance to words based on how frequently they appear in a document and how common they are across the entire collection.

---

💭 Today's Reminder

«"Consistency over motivation." 🔥»

31 days completed.
149 days to go.

One concept at a time.
One project at a time.
One step closer to becoming an AI/ML engineer. 🚀

#AI #MachineLearning #NLP #BagOfWords #Python #ArtificialIntelligence #LearningJourney
