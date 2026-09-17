import re
from collections import Counter

text = """
I am learning Artificial Intelligence.
I love learning AI and Natural Language Processing.
AI is interesting and AI is powerful.
"""

# Convert text to lowercase
text = text.lower()

# Extract words
tokens = re.findall(r"\b[a-z]+\b", text)

print("Tokens:")
print(tokens)

# Count word frequency
word_frequency = Counter(tokens)

print("\nWord Frequency:")
for word, count in word_frequency.items():
    print(word, ":", count)
