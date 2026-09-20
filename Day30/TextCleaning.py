import re

text = "HELLO!!! I am learning NLP, and it's AMAZING!!! 123"
# Convert to lowercase
text = text.lower()

# Remove numbers
text = re.sub(r"\d+", "", text)

# Remove punctuation and special characters
text = re.sub(r"[^a-z\s]", "", text)

# Remove extra spaces
text = re.sub(r"\s+", " ", text).strip()

print("Cleaned Text:")
print(text)
