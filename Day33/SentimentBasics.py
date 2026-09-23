from textblob import TextBlob

texts = [
    "I love learning artificial intelligence.",
    "This project is amazing.",
    "I hate wasting time.",
    "This is a terrible experience.",
    "The book is on the table."
]

for text in texts:
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print("Text:", text)
    print("Polarity:", round(polarity, 2))
    print("Sentiment:", sentiment)
    print("-" * 50)
