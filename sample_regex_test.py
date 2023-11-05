import re

text = "This is a sample text, with some special characters! And spaces too."

# Define a regular expression pattern to match any non-alphanumeric characters as delimiters
pattern = r'[^a-zA-Z0-9]+'

# Use re.split to split the text based on the pattern
words = re.split(pattern, text)

# Remove any empty strings from the result
words = [word for word in words if word]

print(words)
