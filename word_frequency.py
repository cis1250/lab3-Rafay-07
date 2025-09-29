#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re

# Function to check if the input is a valid sentence
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation (period, question mark, exclamation)
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word
    if not re.search(r'\w+', text):
        return False

    return True

# Ask the user to enter a sentence
user_sentence = input("Enter a sentence: ")

# Keep asking until a valid sentence is entered
while not is_sentence(user_sentence):
    print("This does not meet the criteria for a sentence.")  # tell the user it is invalid
    user_sentence = input("Enter a sentence: ")  # ask again

# Convert sentence to lowercase so words are counted without case differences
user_sentence = user_sentence.lower()

# Remove punctuation marks from the sentence
for char in ".!?,":
    user_sentence = user_sentence.replace(char, "")

# Split the sentence into a list of words
words = user_sentence.split()

# Create two empty lists: one for unique words, one for their frequencies
unique_words = []
frequencies = []

# Go through each word in the list
for word in words:
    if word in unique_words:  # check if the word is already in the unique_words list
        index = unique_words.index(word)  # find the position of the word
        frequencies[index] += 1  # increase the frequency at that position
    else:
        unique_words.append(word)  # add new word to unique_words list
        frequencies.append(1)  # start its count at 1

# Print the word frequencies
print("Word frequencies:")
for i in range(len(unique_words)):
    print(unique_words[i] + ":", frequencies[i])
