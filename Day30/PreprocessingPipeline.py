import re

text = """
NLP is AMAZING!!!
I am learning Natural Language Processing in 2026.
"""
# 1. Lowercase
text = text.lower()

# 2. Remove numbers
text = re.sub(r"\d+", "", text)

# 3. Remove punctuation
text = re.sub(r"[^a-z\s]", "", text)

# 4. Remove extra spaces
text = re.sub(r"\s+", " ", text).strip()

# 5. Tokenization
tokens = text.split()

# Simple stop-word list
stop_words = {"is", "am", "in", "the", "and"}

# 6. Remove stop words
filtered_tokens = [
    word for word in tokens
    if word not in stop_words
]

print("Original Text:")
print(text)

print("\nTokens:")
print(tokens)

print("\nAfter Stop Word Removal:")
print(filtered_tokens)
