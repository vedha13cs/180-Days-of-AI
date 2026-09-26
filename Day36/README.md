🧠 Day 36/180 — Word Embeddings

«Teaching machines to understand relationships between words! 🔢🧠»

Welcome to Day 36 of my 180 Days of AI Learning Journey 🚀

Today, I explored Word Embeddings, an important concept in Natural Language Processing (NLP).

Instead of representing a word simply as text, word embeddings represent words as numerical vectors that can capture relationships and similarities between words.

---

🎯 Today's Goal

Today I learned:

- 🔹 What are Word Embeddings?
- 🔹 Why computers need numerical representations of words
- 🔹 What is a vector?
- 🔹 How words can be represented using numbers
- 🔹 How word similarity can be measured
- 🔹 What is cosine similarity?
- 🔹 Where word embeddings are used in AI

---

🤔 What Are Word Embeddings?

A computer cannot directly understand the meaning of a word like:

Python
Machine Learning
AI
Computer

Machine learning models work with numerical data.

So we represent words as vectors of numbers.

For example:

Python → [0.9, 0.8, 0.7]
Java   → [0.8, 0.7, 0.6]
Apple  → [0.2, 0.3, 0.2]

These numbers are called a word vector.

The vector acts as a numerical representation of a word.

---

📐 What Is a Vector?

A vector is simply a collection of numbers.

Example:

[0.8, 0.6, 0.9]

In NLP, these numbers represent features learned from language data.

In real-world embedding models, vectors can contain hundreds or even thousands of dimensions.

---

🧠 Why Are Word Embeddings Important?

Consider these words:

King
Queen
Man
Woman

A good embedding model can learn relationships between these words based on how they appear in language.

Similarly:

Python
Java
JavaScript

may appear in similar programming-related contexts.

This allows AI systems to work with semantic relationships rather than treating every word as completely unrelated.

---

🔢 From Words to Numbers

The basic idea is:

Text
 ↓
Words
 ↓
Numerical Representation
 ↓
Vectors
 ↓
Machine Learning Model

Example:

"I love Python"

can eventually be represented using numerical vectors that a machine learning model can process.

---

📊 Word Similarity

One important use of word embeddings is finding how similar two words are.

For example:

Python ↔ Java

may have a relatively high similarity because both are programming languages.

While:

Python ↔ Banana

would generally be less related.

---

📐 Cosine Similarity

One common method for comparing vectors is Cosine Similarity.

It measures the angle between two vectors.

The basic idea is:

Similar direction → Higher similarity
Different direction → Lower similarity

The formula is:

              A · B
cos(θ) = ─────────────
          ||A|| ||B||

Where:

- "A" = first vector
- "B" = second vector
- "A · B" = dot product
- "||A||" = magnitude of vector A
- "||B||" = magnitude of vector B

---

💻 Today's Python Practice

"word_embeddings_basics.py"

I created simple numerical vectors for words and displayed them.

Example:

word_vectors = {
    "python": [0.9, 0.8, 0.7],
    "java": [0.8, 0.7, 0.6]
}

This helped me understand the basic idea behind representing words numerically.

---

"word_similarity.py"

I used Cosine Similarity to compare two word vectors.

The program calculates how closely the vectors are related.

---

📁 Project Structure

Day-36-Word-Embeddings/
│
├── README.md
├── word_embeddings_basics.py
└── word_similarity.py

---

🌍 Real-World Applications

Word embeddings are used in many NLP applications.

🔎 Search Engines

They can help understand relationships between search terms.

🤖 Chatbots

They help AI systems process the meaning and context of user messages.

🌐 Machine Translation

Embeddings can help represent words across languages.

📄 Text Classification

They can provide numerical representations of text for classification models.

🎬 Recommendation Systems

Similarity between descriptions, reviews, or user-generated text can help improve recommendations.

💬 Sentiment Analysis

Word representations can be used as inputs for models that analyze opinions and emotions.

---

🧩 Popular Word Embedding Techniques

Some important approaches include:

1️⃣ Word2Vec

Developed by researchers at Google, Word2Vec learns word representations from surrounding context.

Two common approaches are:

CBOW
Skip-Gram

2️⃣ GloVe

Global Vectors for Word Representation learns embeddings using global word co-occurrence information.

3️⃣ FastText

FastText represents words using smaller character-level pieces, which can help with rare and previously unseen words.

---

🆚 One-Hot Encoding vs Word Embeddings

One-Hot Encoding| Word Embeddings
Sparse representation| Dense representation
Large vectors| Usually more compact
Does not naturally capture similarity| Can capture relationships
Simple representation| Learned representation
Example: "[1,0,0,0]"| Example: "[0.72,0.31,0.84]"

---

⚠️ Challenges

Word embeddings also have limitations.

🔹 Context

The same word can have different meanings depending on the sentence.

Example:

I went to the bank to deposit money.

versus:

We sat near the river bank.

The word bank has different meanings.

🔹 Bias

Embeddings learned from human-created text can reproduce biases present in the training data.

🔹 Static Embeddings

Traditional embeddings such as Word2Vec generally assign one representation to a word, making context-dependent meanings difficult to represent.

Modern NLP models address this using contextual representations.

---

🧠 Key Learning

Today's biggest takeaway:

«Words can be converted into numerical representations that allow AI models to work with relationships between words.»

Instead of seeing:

Python
Java
Machine Learning

as only text, an AI system can work with their numerical representations.

---

📝 Practice Tasks

Practice 1

Create vectors for:

AI
Machine Learning
Python
Football

Print the vectors.

Practice 2

Calculate the similarity between:

Python ↔ Java

and

Python ↔ Football

Compare the results.

Practice 3

Research and write a short note about:

Word2Vec
GloVe
FastText

---

🔥 Today's Progress

Day 36 / 180

███████░░░░░░░░░░░░░ 20%

✅ Completed

- Day 29 → NLP Fundamentals
- Day 30 → Text Preprocessing
- Day 31 → Bag of Words
- Day 32 → TF-IDF
- Day 33 → Sentiment Analysis
- Day 34 → NLP Text Classification
- Day 35 → Named Entity Recognition
- Day 36 → Word Embeddings 🎯

---

📊 Journey Status

36 / 180 Days Completed

144 Days Remaining

36 ÷ 180 × 100 = 20%

🎯 20% of the journey completed!

---

🌱 Reflection

Today reminded me that AI doesn't understand words in the same way humans do.

It needs a mathematical representation of language before machine learning models can work with it.

From simple words to numerical vectors — this is another step toward understanding how modern NLP systems work. 🤖

---

🚀 What's Next?

Day 37 → Word2Vec

Next, I will explore how Word2Vec learns meaningful word representations from context.

The journey continues... 🔥

«Learn → Practice → Build → Repeat.»

«Consistency over motivation. 💻🚀»
