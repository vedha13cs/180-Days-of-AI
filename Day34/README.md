Day 34 – NLP Text Classification 🤖

This project is part of my NLP (Natural Language Processing) learning journey.

📁 Project Structure

Day-34-NLP-Text-Classification/
│
├── README.md
├── text_classification_basics.py
└── spam_classifier.py

📌 Topics Covered

- Natural Language Processing (NLP)
- Text Classification
- TF-IDF Vectorization
- Logistic Regression
- Multinomial Naive Bayes
- Sentiment Classification
- Spam Message Classification

---

1️⃣ Text Classification using Logistic Regression

File: "text_classification_basics.py"

This program performs simple sentiment classification using Machine Learning.

The model classifies text into:

- Positive
- Negative

Example

"I love learning Python"
→ Positive

"This is a terrible mistake"
→ Negative

Algorithm Used

Logistic Regression

The text is first converted into numerical features using TF-IDF Vectorization, and then Logistic Regression is used to classify the text.

Workflow

Text Data
   ↓
TF-IDF Vectorization
   ↓
Numerical Features
   ↓
Logistic Regression
   ↓
Prediction

Sample Predictions

Text: I enjoy learning machine learning
Prediction: Positive

Text: This is a terrible experience
Prediction: Negative

---

2️⃣ Spam Message Classification

File: "spam_classifier.py"

This program classifies messages into:

- Spam
- Normal

Example

"Congratulations! You won a free prize"
→ Spam

"Please send me the project report"
→ Normal

Algorithm Used

Multinomial Naive Bayes

The messages are converted into numerical features using TF-IDF and then classified using the Multinomial Naive Bayes algorithm.

Workflow

Messages
   ↓
TF-IDF Vectorization
   ↓
Numerical Features
   ↓
Multinomial Naive Bayes
   ↓
Prediction
   ↓
Spam / Normal

Sample Predictions

Message: Congratulations you won a free gift
Prediction: Spam

Message: Please send me your assignment
Prediction: Normal

---

🛠️ Technologies Used

Technology| Purpose
Python| Programming Language
Scikit-learn| Machine Learning
TF-IDF| Text Feature Extraction
Logistic Regression| Text Classification
Multinomial Naive Bayes| Spam Classification

---

📦 Installation

Install Scikit-learn:

pip install scikit-learn

---

▶️ How to Run

Run the text classification program:

python text_classification_basics.py

Run the spam classifier:

python spam_classifier.py

---

🎯 Learning Outcomes

Through this project, I learned:

- Basics of Natural Language Processing
- Text classification using Machine Learning
- TF-IDF Vectorization
- Logistic Regression
- Multinomial Naive Bayes
- Sentiment classification
- Spam message classification
- Making predictions on new text

---

🌍 Real-World Applications

NLP text classification can be used in:

- 📧 Email spam detection
- 😊 Sentiment analysis
- 💬 Chatbots
- 📰 News classification
- ⭐ Review analysis
- 🔍 Text filtering

---

🚀 Future Improvements

- Use a larger real-world dataset
- Add more sentiment categories
- Add training and testing datasets
- Calculate accuracy and other evaluation metrics
- Build a web interface using Flask
- Create a real-time spam detection 


Day 34 Completed! 🚀

Learn → Code → Practice → Build → Repeat 🔥
