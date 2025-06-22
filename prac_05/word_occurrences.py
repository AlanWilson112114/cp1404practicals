"""
CP1404/CP5632 Practical
Count word occurrences in a string
"""

word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    # Count the frequency of each word using the "Look Before You Leap" pattern
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

# Get the list of unique words and sort alphabetically
words = list(word_to_count.keys())
words.sort()

# Find the length of the longest word for aligned printing
max_length = max((len(word) for word in words))
# Print each word with its frequency, aligned by longest word length
for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
