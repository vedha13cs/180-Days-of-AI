from textblob import TextBlob

reviews = [
    "The movie was fantastic and I really enjoyed it.",
    "The story was boring and disappointing.",
    "The movie was okay, nothing special.",
    "Amazing acting and beautiful visuals.",
    "I did not enjoy the movie at all."
]

print("Movie Review Sentiment Analysis\n")

for review in reviews:
    polarity = TextBlob(review).sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    print("Review:", review)
    print("Polarity:", round(polarity, 2))
    print("Result:", sentiment)
    print("-" * 60)
