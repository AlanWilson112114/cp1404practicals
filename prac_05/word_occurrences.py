"""
File: word_occurrences.py
"""

input_text = input("Text: ").strip()

words = input_text.split()

word_frequency = {}

for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

unique_words = sorted(word_frequency.keys())

max_word_length = max(len(word) for word in unique_words)

for word in unique_words:
    frequency = word_frequency[word]
    print(f"{word:{max_word_length}} : {frequency}")
